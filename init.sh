sudo su
apt-get install nginx
pip install gunicorn
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/nginx/sites-enabled/test
sudo /etc/init.d/gunicorn restart
