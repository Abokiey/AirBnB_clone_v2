#!/usr/bin/env bash
# nginx configs

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# make directories
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

#mAke a html file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

#make a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#ownership changes
sudo chown -hR ubuntu:ubuntu /data/

#nginx config
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo nginx -t
sudo service nginx restart
