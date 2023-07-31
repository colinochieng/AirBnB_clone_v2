#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y upgrade

if ! command -v nginx &>/dev/null; then
    sudo apt-get install -y nginx
fi

if ! [ -d '/data/' ]; then
    sudo mkdir /data/
fi

if ! [ -d '/data/web_static/' ]; then
    sudo mkdir /data/web_static/
fi

if ! [ -d '/data/web_static/releases/' ]; then
    sudo mkdir /data/web_static/releases/
fi

if ! [ -d '/data/web_static/shared/' ]; then
    sudo mkdir /data/web_static/shared/
fi

if ! [ -d '/data/web_static/releases/test/' ]; then
    sudo mkdir /data/web_static/releases/test/
fi

echo '<html><body><h1>HBNB TESTING</h1></body></html>' | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/


default_config="
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        # Add custom header
        add_header X-Served-By \$hostname;
        error_page 404 /custom_404.html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                root /var/www/html/;
                try_files \$uri \$uri/ =404;
                rewrite ^/redirect_me(.*)\$ https://www.youtube.com/watch?v=70JD5YTemJc permanent;
        }

        location = /custom_404.html {
                root /var/www/error/;
                internal;
        }

        location /hbnb_static/ {
            alias /data/web_static/current/;
            try_files \$uri \$uri/ =404;
        }
}
"
echo "$default_config" | sudo tee /etc/nginx/sites-available/default >/dev/null

sudo service nginx restart
