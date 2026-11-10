#!/bin/sh
# Daily backup of the database and uploaded photos. Cron: 0 3 * * * /var/www/faujii/deploy/backup.sh
set -e
DEST=/var/backups/faujii; mkdir -p "$DEST"
sqlite3 /var/www/faujii/instance/faujii.db ".backup '$DEST/faujii-$(date +%F).db'"
tar czf "$DEST/images-$(date +%F).tgz" -C /var/www/faujii/static images
find "$DEST" -mtime +14 -delete
