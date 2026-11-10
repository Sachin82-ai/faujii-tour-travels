import os
from datetime import datetime
from urllib.parse import quote

from flask import Flask, render_template
from markupsafe import Markup, escape

from config import Config
from models import db
from models.content import NAV
from routes.admin import bp as admin_bp
from routes.main import bp as main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_db()
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    def t(pair):
        """Render an (English, Hindi) tuple; CSS shows the active language."""
        en, hi = pair
        return Markup(f'<span class="l-en">{escape(en)}</span><span class="l-hi">{escape(hi)}</span>')

    def en(pair):
        return pair[0]

    @app.context_processor
    def inject():
        b = db.settings()
        wa = f"https://wa.me/{b['whatsapp']}"
        return dict(
            t=t, en=en, B=b, now_year=datetime.now().year, NAV=NAV,
            tel=f"tel:{b['phone']}",
            wa_link=lambda msg="Hello Faujii Tour & Travels, I would like to enquire about a tour.":
                f"{wa}?text={quote(msg)}",
            maps_link="https://www.google.com/maps/search/?api=1&query=" + quote(b["map_query"]),
            maps_embed="https://www.google.com/maps?q=" + quote(b["map_query"]) + "&output=embed",
        )

    @app.after_request
    def headers(resp):
        resp.headers.setdefault("X-Content-Type-Options", "nosniff")
        resp.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        resp.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        return resp

    @app.errorhandler(404)
    def not_found(_):
        return render_template("404.html", page="", title="Page not found"), 404

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
