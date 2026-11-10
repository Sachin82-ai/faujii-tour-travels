"""Smoke tests: python test_site.py  (uses a temporary database)"""
import io, os, re, tempfile
os.environ["DB_PATH"] = os.path.join(tempfile.mkdtemp(), "t.db")
os.environ["ADMIN_PASSWORD"] = "secret123"
from PIL import Image
from app import app
app.config["SESSION_COOKIE_SECURE"] = False
c = app.test_client()

def ok(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond: raise SystemExit(1)

for p in ["/", "/about", "/services", "/braj-darshan", "/packages", "/vehicles", "/destinations", "/gallery",
          "/travel-guide", "/contact", "/contact.html", "/terms", "/privacy", "/sitemap.xml", "/robots.txt"]:
    ok(c.get(p).status_code == 200, "GET " + p)
ok(c.get("/nope").status_code == 404, "404 page")
r = c.get("/contact").get_data(as_text=True)
ok("tel:8278618368" in r and "wa.me/918278618368" in r and "<form" not in r, "contact links, no form")
ok("Contact for Price" in c.get("/packages").get_data(as_text=True), "no invented prices")
ok("g01.jpg" in c.get("/gallery").get_data(as_text=True), "gallery from db")

ok(c.get("/admin/").status_code == 302, "admin requires login")
def token(path):
    return re.search(r'name="csrf" value="([^"]+)"', c.get(path).get_data(as_text=True)).group(1)
ok(c.post("/admin/login", data={"password": "x", "csrf": token("/admin/login")}).status_code == 200, "wrong password rejected")
ok(c.post("/admin/login", data={"password": "x"}).status_code == 400, "csrf enforced")
ok(c.post("/admin/login", data={"password": "secret123", "csrf": token("/admin/login")}).status_code == 302, "login ok")
for k in ["", "settings", "destinations", "packages", "vehicles", "gallery", "guides", "faqs"]:
    ok(c.get("/admin/" + k).status_code == 200, "admin /" + k)

t = token("/admin/packages/new")
r = c.post("/admin/packages/new", data={"csrf": t, "name__en": "Test Tour", "name__hi": "", "places__en": "X", "places__hi": "",
    "duration__en": "1 day", "duration__hi": "", "price__en": "Rs 5000", "price__hi": "", "published": "on", "icon": "", "color": "#101B50"})
ok(r.status_code == 302, "create package")
pk = c.get("/packages").get_data(as_text=True)
ok("Test Tour" in pk and "Rs 5000" in pk, "new package + price visible publicly")
c.post("/admin/packages/test-tour/toggle", data={"csrf": t})
ok("Test Tour" not in c.get("/packages").get_data(as_text=True), "hide package")
c.post("/admin/packages/test-tour/delete", data={"csrf": t})
ok(c.get("/admin/packages/test-tour/edit").status_code == 404, "delete package")

buf = io.BytesIO(); Image.new("RGB", (900, 600), "red").save(buf, "PNG"); buf.seek(0)
r = c.post("/admin/gallery/new", data={"csrf": t, "caption__en": "Upload test", "caption__hi": "", "cat": "braj", "published": "on",
                                        "image": (buf, "x.png")}, content_type="multipart/form-data")
ok(r.status_code == 302, "gallery upload")
fn = re.search(r"images/gallery/(u\d+\.jpg)", c.get("/gallery").get_data(as_text=True)).group(1)
ok(os.path.exists(os.path.join(app.static_folder, "images", "gallery", fn)), "uploaded file saved")
c.post(f"/admin/gallery/{fn}/delete", data={"csrf": t})
ok(not os.path.exists(os.path.join(app.static_folder, "images", "gallery", fn)), "uploaded file removed")

c.post("/admin/settings", data={"csrf": t, "phone": "9999999999", "phone_display": "99999 99999", "whatsapp": "919999999999",
       "map_query": "Mathura", "name__en": "Faujii Tour & Travels", "name__hi": "", "owner__en": "Owner", "owner__hi": "",
       "address__en": "A", "address__hi": "", "timings__en": "9-6", "timings__hi": ""})
ok("tel:9999999999" in c.get("/contact").get_data(as_text=True), "contact details editable")
print("ALL OK")
