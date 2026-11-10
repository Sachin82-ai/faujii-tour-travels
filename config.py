import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
    SITE_URL = os.environ.get("SITE_URL", "https://www.faujiitourtravels.com")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")   # admin is disabled until this is set
    GA_ID = os.environ.get("GA_ID", "")                     # Google Analytics ID, e.g. G-XXXXXXXXXX (optional)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.environ.get("FLASK_DEBUG") != "1" and SITE_URL.startswith("https")
    MAX_CONTENT_LENGTH = 12 * 1024 * 1024                   # upload limit
