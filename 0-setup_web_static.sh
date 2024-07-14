#!/usr/bin/env bash
# Set up your web servers for the deployment of web_static

# Install nginx
apt update -y
apt install nginx -y

# Create the file structure
mkdir /data/web_static/releases/test/ /data/web_static/shared /data/web
touch /data/web_static/releases/test/index.html
# Create a symbolic link
ln -s -f /data/web_static/releases/test/ /data/webstatic/current
# Change ownership
chown -R ubuntu:ubuntu /data/
sed '/server {\n/\tlocation /hbnb_static/ {\n\troot /data/web_static/current/;\n\talias /data/web_static/current/hbnb_static/;\n\t autoindex off;\n}'
nginx -s reload
