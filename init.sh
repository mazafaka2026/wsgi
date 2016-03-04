sudo apt-get install nginx
sudo pip install gunicorn
sudo git clone http://github.com/mazafaka2026/conf.git /home/box/web/conf/
sudo ln -s /home/box/web/conf/nginx_upstream.conf  /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/nginx/sites-enabled/test
#sudo /etc/init.d/gunicorn restart
