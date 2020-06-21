
sudo unlink /etc/nginx/sites-enabled/default
sudo rm -rf /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo /etc/init.d/nginx restart

sudo rm -rf /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn restart 
#sudo gunicorn -c /etc/gunicorn.d/hello.py hello:application
gunicorn --bind='0.0.0.0:8080' hello:wsgi_application

sudo /etc/init.d/mysql start
