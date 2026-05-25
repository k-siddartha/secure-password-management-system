#!/bin/bash
DATE=$(date +%Y%m%d)
tar -czf /tmp/vaultwarden-backup-$DATE.tar.gz ./vw-data/
gpg --symmetric --cipher-algo AES256 /tmp/vaultwarden-backup-$DATE.tar.gz
echo "Backup created: vaultwarden-backup-$DATE.tar.gz.gpg"
