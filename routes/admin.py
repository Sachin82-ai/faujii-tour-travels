"""Private admin panel. Not customer-facing: only the business owner logs in here."""
import hmac
import re
import secrets
import time
from functools import wraps

from flask import (Blueprint, abort, current_app, flash, redirect, render_template, request,
                   session, url_for)
from PIL import Image

from models import content as C
from models import db

bp = Blueprint("admin", __name__, url_prefix="/admin", template_folder="../admin/templates")

PAIR, AREA, TEXT, COLOR = "pair", "area", "text", "color"
ICON_HELP = "Font Awesome icon class, e.g. fa-landmark"

SCHEMA = {
    "destinations": dict(title="Destinations", folder="destinations", image=True, name_key="name", fields=[
        ("name", "Name", PAIR), ("tag", "Tagline", PAIR), ("about", "Introduction", AREA),
        ("sig", "Historical / religious significance", AREA), ("location", "Location", PAIR),
        ("duration", "Suggested visiting duration", PAIR), ("nearby", "Nearby attractions", PAIR),
        ("icon", ICON_HELP, TEXT), ("color", "Placeholder colour", COLOR)]),
    "packages": dict(title="Tour Packages", folder="packages", image=True, name_key="name", fields=[
        ("name", "Package name", PAIR), ("places", "Places covered", PAIR), ("duration", "Duration", PAIR),
        ("price", "Price (leave empty to show 'Contact for Price')", PAIR),
        ("icon", ICON_HELP, TEXT), ("color", "Placeholder colour", COLOR)]),
    "vehicles": dict(title="Vehicles", folder="vehicles", image=True, name_key="name", fields=[
        ("name", "Vehicle / model", PAIR), ("ac", "AC / Non-AC", PAIR), ("seats", "Passenger & luggage capacity", PAIR),
        ("use", "Suitable journeys", PAIR), ("icon", ICON_HELP, TEXT), ("color", "Placeholder colour", COLOR)]),
    "guides": dict(title="Travel Guide Articles", folder=None, image=False, name_key="title", fields=[
        ("title", "Title", PAIR), ("body", "Article text", AREA)]),
    "faqs": dict(title="FAQs", folder=None, image=False, name_key="q", fields=[
        ("q", "Question", PAIR), ("a", "Answer", AREA)]),
    "gallery": dict(title="Gallery Photos", folder="gallery", image=True, name_key="caption", fields=[
        ("caption", "Caption", PAIR)]),
}

SETTINGS_FIELDS = [
    ("name", "Business name", PAIR), ("owner", "Owner / contact person", PAIR),
    ("phone", "Phone (digits only, for tel: link)", TEXT), ("phone_display", "Phone (as displayed)", TEXT),
    ("whatsapp", "WhatsApp number with country code, e.g. 918278618368", TEXT),
    ("address", "Address", PAIR), ("map_query", "Google Maps search text", TEXT), ("timings", "Business timings", PAIR),
    ("facebook", "Facebook URL", TEXT), ("instagram", "Instagram URL", TEXT), ("youtube", "YouTube URL", TEXT),
]

_attempts = {}


# ---------- helpers ----------
def csrf_token():
    if "csrf" not in session:
        session["csrf"] = secrets.token_hex(16)
    return session["csrf"]


def login_required(f):
    @wraps(f)
    def wrapper(*a, **kw):
        if not session.get("admin"):
            return redirect(url_for("admin.login", next=request.path))
        return f(*a, **kw)
    return wrapper


@bp.before_request
def protect():
    if request.method == "POST" and not hmac.compare_digest(request.form.get("csrf", ""), session.get("csrf", "x")):
        abort(400, "Bad CSRF token")


@bp.after_request
def no_cache(resp):
    resp.headers["Cache-Control"] = "no-store"
    resp.headers["X-Robots-Tag"] = "noindex, nofollow"
    return resp


@bp.app_context_processor
def inject():
    return dict(csrf=csrf_token, SCHEMA=SCHEMA)


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:50] or "item"


def parse(fields, form):
    data = {}
    for key, _, typ in fields:
        if typ in (PAIR, AREA):
            en, hi = form.get(key + "__en", "").strip(), form.get(key + "__hi", "").strip()
            data[key] = [en, hi or en] if (en or hi) else None
        else:
            data[key] = form.get(key, "").strip()
    return data


def save_image(file, folder, id_):
    """Convert any uploaded image to an optimised JPG at static/images/<folder>/<id>.jpg."""
    import os
    try:
        im = Image.open(file.stream)
        im.load()
    except Exception:
        return False
    im = im.convert("RGB")
    if im.width > 1600:
        im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
    d = os.path.join(current_app.static_folder, "images", folder)
    os.makedirs(d, exist_ok=True)
    im.save(os.path.join(d, id_ + ".jpg") if not id_.endswith(".jpg") else os.path.join(d, id_), "JPEG", quality=82, optimize=True, progressive=True)
    return True


def kind_or_404(kind):
    if kind not in SCHEMA:
        abort(404)
    return SCHEMA[kind]


# ---------- auth ----------
@bp.route("/login", methods=["GET", "POST"])
def login():
    pw = current_app.config["ADMIN_PASSWORD"]
    if not pw:
        return render_template("login.html", disabled=True)
    ip = request.remote_addr
    tries = [t for t in _attempts.get(ip, []) if t > time.time() - 600]
    if request.method == "POST":
        if len(tries) >= 5:
            flash("Too many attempts. Try again in 10 minutes.", "danger")
        elif hmac.compare_digest(request.form.get("password", ""), pw):
            session.clear(); session["admin"] = True; csrf_token()
            nxt = request.args.get("next", "")
            return redirect(nxt if nxt.startswith("/admin") else url_for("admin.dashboard"))
        else:
            tries.append(time.time()); flash("Wrong password.", "danger")
        _attempts[ip] = tries
    return render_template("login.html", disabled=False)


@bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("admin.login"))


# ---------- screens ----------
@bp.route("/")
@login_required
def dashboard():
    counts = {k: len(db.items(k, published_only=False)) for k in SCHEMA}
    return render_template("dashboard.html", counts=counts)


@bp.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    if request.method == "POST":
        db.save_settings(parse(SETTINGS_FIELDS, request.form))
        flash("Contact details saved.", "success")
        return redirect(url_for("admin.settings"))
    return render_template("edit.html", title="Contact Details", fields=SETTINGS_FIELDS, d=db.settings(),
                           kind=None, is_new=False, image=False, back=url_for("admin.dashboard"))


@bp.route("/<kind>")
@login_required
def listing(kind):
    s = kind_or_404(kind)
    return render_template("list.html", kind=kind, s=s, rows=db.items(kind, published_only=False))


@bp.route("/<kind>/new", methods=["GET", "POST"])
@bp.route("/<kind>/<id_>/edit", methods=["GET", "POST"])
@login_required
def edit(kind, id_=None):
    s = kind_or_404(kind)
    is_new = id_ is None
    d = {} if is_new else db.item(kind, id_)
    if d is None:
        abort(404)
    if request.method == "POST":
        data = parse(s["fields"], request.form)
        published = bool(request.form.get("published"))
        pos = request.form.get("pos", type=int)
        f = request.files.get("image")
        has_file = bool(f and f.filename)
        if kind == "gallery":
            data["cat"] = request.form.get("cat", "braj")
            if is_new:
                if not has_file:
                    flash("Please choose a photo.", "danger")
                    return render_template("edit.html", title="Add Gallery Photo", fields=s["fields"], d=data, kind=kind,
                                           is_new=True, image=True, back=url_for("admin.listing", kind=kind), cats=C.GALLERY_CATEGORIES)
                id_ = f"u{int(time.time())}.jpg"
                data["file"] = id_
            else:
                data["file"] = id_
        elif is_new:
            first = (data.get(s["name_key"]) or [""])[0]
            if not first:
                flash("Name / title (English) is required.", "danger")
                return render_template("edit.html", title="New " + s["title"], fields=s["fields"], d=data, kind=kind,
                                       is_new=True, image=s["image"], back=url_for("admin.listing", kind=kind))
            base = slugify(first); id_ = base; n = 2
            while db.item(kind, id_):
                id_ = f"{base}-{n}"; n += 1
        if kind in ("destinations", "packages", "vehicles"):
            data["icon"] = data.get("icon") or "fa-location-dot"
            data["color"] = data.get("color") or "#101B50"
        if has_file and not save_image(f, s["folder"], id_):
            flash("That file is not a valid image.", "danger")
            return redirect(request.url)
        db.save(kind, id_, data, published, pos)
        flash("Saved.", "success")
        return redirect(url_for("admin.listing", kind=kind))
    return render_template("edit.html", title=("New " if is_new else "Edit ") + s["title"], fields=s["fields"], d=d, kind=kind,
                           is_new=is_new, image=s["image"], back=url_for("admin.listing", kind=kind),
                           cats=C.GALLERY_CATEGORIES, id_=id_)


@bp.route("/<kind>/<id_>/toggle", methods=["POST"])
@login_required
def toggle(kind, id_):
    kind_or_404(kind)
    d = db.item(kind, id_) or abort(404)
    db.save(kind, id_, d, not d["published"])
    return redirect(url_for("admin.listing", kind=kind))


@bp.route("/<kind>/<id_>/delete", methods=["POST"])
@login_required
def delete(kind, id_):
    s = kind_or_404(kind)
    db.delete(kind, id_)
    if kind == "gallery":
        import os
        p = os.path.join(current_app.static_folder, "images", "gallery", id_)
        if os.path.isfile(p):
            os.remove(p)
    flash("Deleted.", "success")
    return redirect(url_for("admin.listing", kind=kind))
