# Deploying Faujii Tour & Travels (Ubuntu VPS)

1. **Domain + VPS**: buy a domain (e.g. faujiitourtravels.com) and an Ubuntu 22.04/24.04 VPS.
2. **DNS**: create `A` records for `@` and `www` pointing to the VPS IP.
3. **Server basics**:
   ```
   sudo apt update && sudo apt install -y python3-venv nginx sqlite3 certbot python3-certbot-nginx ufw git
   sudo ufw allow OpenSSH && sudo ufw allow 'Nginx Full' && sudo ufw enable
   ```
4. **Upload the code** (GitHub or scp) to `/var/www/faujii`:
   ```
   sudo git clone <your-repo-url> /var/www/faujii     # or copy the folder
   ```
5. **Python environment**:
   ```
   cd /var/www/faujii && sudo python3 -m venv venv
   sudo venv/bin/pip install -r requirements.txt
   sudo mkdir -p instance && sudo chown -R www-data:www-data instance static/images
   ```
6. **Secrets**: `sudo cp .env.example /etc/faujii.env`, edit it (SECRET_KEY, ADMIN_PASSWORD, SITE_URL), then `sudo chmod 600 /etc/faujii.env`.
7. **Run with Gunicorn**:
   ```
   sudo cp deploy/faujii.service /etc/systemd/system/
   sudo systemctl daemon-reload && sudo systemctl enable --now faujii
   ```
8. **Nginx**: copy `deploy/nginx.conf` to `/etc/nginx/sites-available/faujii` (edit domain), then
   ```
   sudo ln -s /etc/nginx/sites-available/faujii /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx
   ```
9. **HTTPS**: `sudo certbot --nginx -d faujiitourtravels.com -d www.faujiitourtravels.com` (auto-renews).
10. **Test** on phone and desktop: all pages, call/WhatsApp buttons, `/admin` login, `/sitemap.xml`.
11. **Backups**: `sudo chmod +x deploy/backup.sh`, add to root crontab: `0 3 * * * /var/www/faujii/deploy/backup.sh`.
12. **Updates**: `cd /var/www/faujii && sudo git pull && sudo systemctl restart faujii`.

## After launch (SEO)
- Google Search Console: add the domain, submit `https://<domain>/sitemap.xml`.
- Google Business Profile: create/claim the listing with the same name, address and phone (8278618368).
- Optional analytics: set `GA_ID` in `/etc/faujii.env` (the privacy page updates automatically).
- Add real photos via Admin > Gallery; give them clear captions (used as alt text).
