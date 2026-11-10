# Faujii Tour & Travels website

Flask + SQLite site: 10 public pages, Terms/Privacy/404, English/Hindi toggle, no customer forms,
and a private admin panel at `/admin`.

## Run locally (Windows)
```
py -m pip install -r requirements.txt
$env:ADMIN_PASSWORD="choose-a-password"; $env:FLASK_DEBUG="1"
py app.py            # site: http://127.0.0.1:5000   admin: http://127.0.0.1:5000/admin
py test_site.py      # smoke tests (use a temporary database)
```
The database (`instance/faujii.db`) is created on first run from `models/content.py`.
After that, edit content in the admin panel, not in `content.py`.

## Admin panel
Log in at `/admin` (disabled until `ADMIN_PASSWORD` is set). Manage destinations, packages (prices),
vehicles, gallery uploads, travel guides, FAQs and contact details. "Hide" removes an item from the
site without deleting it. Uploaded photos are converted to optimised JPG.

## Photos
Destination/package/vehicle photos live in `static/images/<folder>/<id>.jpg`; upload them in the admin panel.
Credits for the downloaded stock photos: `static/images/CREDITS.md`.

## Before launch
Add real prices, confirm timings, real fleet details and photos, review Hindi text and the Terms/Privacy drafts.
Deployment steps: `deploy/DEPLOY.md`.
