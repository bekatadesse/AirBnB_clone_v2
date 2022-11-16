#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hellow World!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current


chown -R ubuntu:ubuntu /data/

printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root /etc/nginx/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        location /hbnb_static {
                alias /data/web_static/current;
                index index.html index.htm;
        }

        server_name _;
        location / {
                try_files $uri $uri/ =404;
        }
}" > /etc/nginx/sites-available/default
service nginx restart
