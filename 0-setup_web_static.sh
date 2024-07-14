#!/usr/bin/env bash
# Set up your web servers for the deployment of web_static

#Exit immediately if a command exits with a non-zero status

set -e

# Install nginx
apt update -y
apt install nginx -y

# Create the file structure
mkdir -p /data/web_static/releases/test/ /data/web_static/shared /data/web
echo "<html>
        <head></head>
        <body>Holberton School</body>
      </html>" > /data/web_static/releases/test/index.html
# Create a symbolic link
ln -s -f /data/web_static/releases/test/ /data/web_static/current
# Change ownership
chown -R ubuntu:ubuntu /data/
#Update Nginx configuration to serve the content
if grep -q "location /hbnb_static/" /etc/nginx/nginx.conf; then
	echo ""
else 
	sed -i '/server {/a\
	        location /hbnb_static/ {\n\
			alias /data/web_static/current/;
			autoindex off;\n}' /etc/nginx/nginx.conf
fi
if nginx -t; then
	sudo service nginx restart
else
	exit
fi
