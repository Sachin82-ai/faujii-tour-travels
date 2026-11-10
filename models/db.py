"""SQLite storage. Each content item is a JSON document in `items`; site settings live in `settings`.
The first run seeds everything from models/content.py."""
import json
import os
import sqlite3

from models import content as C

DB_PATH = os.environ.get("DB_PATH") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "instance", "faujii.db")

KINDS = ("destinations", "packages", "vehicles", "gallery", "guides", "faqs")


def conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def init_db():
    with conn() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS items(
            kind TEXT NOT NULL, id TEXT NOT NULL, pos INTEGER NOT NULL DEFAULT 0,
            published INTEGER NOT NULL DEFAULT 1, data TEXT NOT NULL, PRIMARY KEY(kind, id));
        CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY, value TEXT NOT NULL);
        """)
        if c.execute("SELECT COUNT(*) FROM items").fetchone()[0] == 0:
            seed(c)


def seed(c):
    def put(kind, rows):
        for n, (id_, data) in enumerate(rows):
            c.execute("INSERT INTO items(kind,id,pos,data) VALUES(?,?,?,?)", (kind, id_, n, json.dumps(data, ensure_ascii=False)))
    put("destinations", [(d["id"], d) for d in C.DESTINATIONS])
    put("packages", [(p["id"], p) for p in C.PACKAGES])
    put("vehicles", [(v["id"], v) for v in C.VEHICLES])
    put("guides", [(g["id"], g) for g in C.GUIDES])
    put("gallery", [(f, dict(file=f, cat=cat, caption=[cap, cap])) for f, cat, cap in C.GALLERY])
    put("faqs", [(f"q{i}", dict(q=q, a=a)) for i, (q, a) in enumerate(C.FAQS, 1)])


def items(kind, published_only=True):
    q = "SELECT id,published,data FROM items WHERE kind=?" + (" AND published=1" if published_only else "") + " ORDER BY pos,rowid"
    with conn() as c:
        out = []
        for r in c.execute(q, (kind,)):
            d = json.loads(r["data"]); d["id"] = r["id"]; d["published"] = bool(r["published"])
            out.append(d)
        return out


def item(kind, id_):
    with conn() as c:
        r = c.execute("SELECT id,published,pos,data FROM items WHERE kind=? AND id=?", (kind, id_)).fetchone()
    if not r:
        return None
    d = json.loads(r["data"]); d["id"] = r["id"]; d["published"] = bool(r["published"]); d["pos"] = r["pos"]
    return d


def save(kind, id_, data, published=True, pos=None):
    data = {k: v for k, v in data.items() if k not in ("id", "published", "pos")}
    with conn() as c:
        old = c.execute("SELECT pos FROM items WHERE kind=? AND id=?", (kind, id_)).fetchone()
        if pos is None:
            pos = old["pos"] if old else (c.execute("SELECT COALESCE(MAX(pos),-1)+1 FROM items WHERE kind=?", (kind,)).fetchone()[0])
        c.execute("INSERT OR REPLACE INTO items(kind,id,pos,published,data) VALUES(?,?,?,?,?)",
                  (kind, id_, pos, 1 if published else 0, json.dumps(data, ensure_ascii=False)))


def delete(kind, id_):
    with conn() as c:
        c.execute("DELETE FROM items WHERE kind=? AND id=?", (kind, id_))


def settings():
    """Business settings: defaults from content.py overridden by admin edits."""
    s = dict(C.BUSINESS)
    with conn() as c:
        for r in c.execute("SELECT key,value FROM settings"):
            s[r["key"]] = json.loads(r["value"])
    return s


def save_settings(values):
    with conn() as c:
        for k, v in values.items():
            c.execute("INSERT OR REPLACE INTO settings(key,value) VALUES(?,?)", (k, json.dumps(v, ensure_ascii=False)))
