from flask import Blueprint, Response, current_app, render_template, url_for

from models import content as C
from models import db

bp = Blueprint("main", __name__)

PAGES = [
    ("/", "home"), ("/about", "about"), ("/services", "services"), ("/braj-darshan", "braj"),
    ("/packages", "packages"), ("/vehicles", "vehicles"), ("/destinations", "destinations"),
    ("/gallery", "gallery"), ("/travel-guide", "guide"), ("/contact", "contact"),
    ("/terms", "terms"), ("/privacy", "privacy"),
]


def D():
    return {d["id"]: d for d in db.items("destinations")}


@bp.route("/")
def home():
    return render_template(
        "index.html", page="home",
        title="Faujii Tour & Travels | Braj Darshan, Mathura Vrindavan Taxi",
        desc="Braj Darshan taxi and tour packages from Mathura. Vrindavan, Govardhan, Barsana, Agra and outstation trips. Call 8278618368.",
        packages=db.items("packages")[:4], dests=db.items("destinations")[:6], vehicles=db.items("vehicles"),
        why=C.WHY, routes=C.ROUTES, faqs=db.items("faqs"))


@bp.route("/about")
def about():
    return render_template("about.html", page="about", title="About Us | Faujii Tour & Travels",
                           desc="About Faujii Tour & Travels, a Mathura travel service run by Ex/Havaldar Upender Singh.")


@bp.route("/services")
def services():
    return render_template("services.html", page="services", title="Our Services | Faujii Tour & Travels",
                           desc="Local taxi, Braj Darshan, outstation, airport transfer, wedding and corporate travel in Mathura.",
                           services=C.SERVICES)


@bp.route("/braj-darshan")
def braj():
    d = D()
    groups = [(name, [d[i] for i in ids if i in d], extra) for name, ids, extra in C.BRAJ_GROUPS]
    return render_template("braj-darshan.html", page="braj", title="Braj Darshan Taxi Service | Faujii Tour & Travels",
                           desc="Braj Darshan tour: Nandgaon, Barsana, Govardhan, Gokul, Raman Reti, Brahmand Ghat, Chaurasi Khamba and Janmasthan.",
                           groups=groups, extra=C.BRAJ_EXTRA)


@bp.route("/packages")
def packages():
    return render_template("packages.html", page="packages", title="Braj Tour Packages | Faujii Tour & Travels",
                           desc="Mathura, Vrindavan, Braj Darshan, Agra and custom outstation tour packages.",
                           packages=db.items("packages"), inc=C.PACKAGE_INCLUDES, exc=C.PACKAGE_EXCLUDES, pveh=C.PACKAGE_VEHICLES)


@bp.route("/vehicles")
def vehicles():
    return render_template("vehicles.html", page="vehicles", title="Our Vehicles | Faujii Tour & Travels",
                           desc="AC and Non-AC cars for sightseeing and outstation travel from Mathura.", vehicles=db.items("vehicles"))


@bp.route("/destinations")
def destinations():
    return render_template("destinations.html", page="destinations", title="Destinations | Faujii Tour & Travels",
                           desc="Mathura, Vrindavan, Govardhan, Barsana, Nandgaon, Gokul, Agra and Fatehpur Sikri.",
                           dests=db.items("destinations"))


@bp.route("/gallery")
def gallery():
    return render_template("gallery.html", page="gallery", title="Gallery | Faujii Tour & Travels",
                           desc="Photos of vehicles, Braj Darshan and destinations.", cats=C.GALLERY_CATEGORIES, items=db.items("gallery"))


@bp.route("/travel-guide")
def guide():
    return render_template("travel-guide.html", page="guide", title="Travel Guide | Faujii Tour & Travels",
                           desc="Guides to Mathura, Vrindavan, Govardhan Parikrama, Barsana and Agra.", guides=db.items("guides"))


@bp.route("/contact")
def contact():
    return render_template("contact.html", page="contact", title="Contact Us | Faujii Tour & Travels",
                           desc="Call 8278618368 or WhatsApp Faujii Tour & Travels, Girdharpur, Govardhan Chauraha, Mathura.")


@bp.route("/contact.html")
def contact_html():
    return contact()


@bp.route("/terms")
def terms():
    return render_template("terms.html", page="terms", title="Terms & Conditions | Faujii Tour & Travels", desc="Terms and conditions.")


@bp.route("/privacy")
def privacy():
    return render_template("privacy.html", page="privacy", title="Privacy Policy | Faujii Tour & Travels", desc="Privacy policy.")


@bp.route("/robots.txt")
def robots():
    base = current_app.config["SITE_URL"]
    return Response(f"User-agent: *\nDisallow: /admin\nAllow: /\nSitemap: {base}/sitemap.xml\n", mimetype="text/plain")


@bp.route("/sitemap.xml")
def sitemap():
    base = current_app.config["SITE_URL"]
    urls = "".join(f"<url><loc>{base}{p}</loc></url>" for p, _ in PAGES)
    return Response(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>',
                    mimetype="application/xml")
