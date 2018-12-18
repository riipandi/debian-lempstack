server {
    listen 80;
    listen 443 ssl http2;

    server_name ~^(?<user>[a-zA-Z0-9-]+)\.domain\.tld$;

    root /srv/HOSTNAME/public;
    access_log /var/log/nginx/HOSTNAME-access.log main;
    error_log  /var/log/nginx/HOSTNAME-error.log warn;

    ssl_certificate         /etc/letsencrypt/live/HOSTNAME/fullchain.pem;
    ssl_certificate_key     /etc/letsencrypt/live/HOSTNAME/privkey.pem;
    ssl_trusted_certificate /etc/ssl/certs/chain.pem;

    include server.d/wpmu.conf;
}