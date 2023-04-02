# SocialNetworkSite
a social network site built using django
TAILWIND NOTES
-how to run tailwind
-cd jstools
-npx tailwindcss -i ./src/input.css -o ../jobssite/jobs/static/jobs/css/styles.css --watch

CREATING VIRTUAL ENV NORMAL WAY
python3 -m venv jopsite-env

ACTIVATE VENV
-run the command in the folder S24PROJECT on terminal
source jobsite-env/bin/activate

on windows
cd blogpersonal-env
Scripts/activate

UPDATE PIP
python -m pip install --upgrade pip

UPDATE PILLOW
python -m pip install --upgrade pillow

LIST VENV PACKAGES
pip freeze --local

CREATING A REQUIREMENTS.TXT
pip3 freeze > requirements.txt

FOR LOCAL PACKAGES ONLY IN THE ENV
pip freeze --local  > requirements.txt





--------------------------------------------------------
DATABASES

-postgre driver
pip install psycopg2-binary==2.8.6

CREATE DATABASE xxxx;
CREATE USER wiz WITH PASSWORD  'xxxxxxx;

ALTER ROLE wiz SET client_encoding TO 'utf8';
ALTER ROLE wiz SET default_transaction_isolation TO 'read committed';
ALTER ROLE wiz SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE xxx TO wiz;


. . .

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': 'wiz',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

. . .
---------------------------------------------------------------
GIT
-force git pull
git reset --hard HEAD
git pull
-------------------------------------------------------------
TO BE ROOT
sudo bash
su


POSTGRESQL COMMANDS
-accessing postgresql prompt
sudo -u postgres psql
sudo -u wiz psql
sudo -u wiz psql xxxxuser

-list databases
\l
-list tables
\dt
-connect to database
\c DBNAME

-list all users
\du

-exit
\q
-Creating a New Database
createdb xxx
CREATE DATABASE xxxx;
sudo -u postgres psql -c 'create database xxx;'
sudo -u postgres psql -c 'grant all privileges on database xxxx to wiz;'

-delete database 
dropdb xxxx
or
DROP DATABASE xxxx;

-set password for user
ALTER USER wiz WITH PASSWORD '1234567wiz';

LINUX


GUNICORN
-testing hgunicorn on django 
gunicorn --bind 0.0.0.0:8000 project.wsgi

-see status of gunicorn
sudo systemctl status gunicorn

-logs
sudo journalctl -u gunicorn


-config file 
sudo nano /etc/systemd/system/gunicorn.service


-cointents of config file 
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=name
Group=www-data
WorkingDirectory=/home/dev/xxxx
ExecStart=/home/dev/xxxx-env/bin/gunicorn \
          --access-logfile - \
          --workers 5 \
          --timeout 600 \
          --bind unix:/run/gunicorn.sock \
          xxxx_freedata_django.wsgi:application


[Install]
WantedBy=multi-user.target


[Install]
WantedBy=multi-user.target



NGNINX


NGNINX CONFIG FILE
/etc/nginx/nginx.conf
-If it does not exist there, it may also be at 
/usr/local/nginx/conf/nginx.conf 
-or 
/usr/local/etc/nginx/nginx.conf


-second config file 
found on 
sudo nano /etc/nginx/sites-available/xxxx

server {
    listen 80;
    server_name 'IP GOES HERE';

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/dev/xxxx;
    }
    
    location /media/ {
            root /home/dev/xxxx;
        }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}


LOGS
sudo tail -F /var/log/nginx/error.log
tail /var/log/nginx/access.log.1
tail /var/log/nginx/access.log
tail /var/log/nginx/error.log
tail /var/log/nginx/error.log.1
tail /var/log/syslog

Check the Nginx process logs: sudo journalctl -u nginx
Check the Nginx access logs: sudo less /var/log/nginx/access.log
Check the Nginx error logs: sudo less /var/log/nginx/error.log
Check the Gunicorn application logs: sudo journalctl -u gunicorn
Check the Gunicorn socket logs: sudo journalctl -u gunicorn.socket

press Q to exit log condole at times

RESTART NGNINX
sudo systemctl restart nginx
OR

sudo service nginx restart
GUNICORN
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

COMBINED
sudo systemctl restart nginx
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

---------------------------------------------------------------------------------
RUNING CELERY ON THE BACKGROUND
-Install Supervisor 
sudo apt-get install supervisor

-restart it
sudo service supervisor restart

Config file 
sudo nano  /etc/supervisor/conf.d/celery.conf


-Infor in celery.conf LOCAL ENVIRONMENT

[program:celery]
directory = /home/USER/Desktop/xxxx/xxxx/
command = /home/USER/Desktop/xxxx/xxxx-env/bin/celery -A xxxx_freedata_django worker --
loglevel=INFO
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/long.err.log
stdout_logfile=/var/log/long.out.log

-Infor in celery.conf PRODUCTION ENVIRONMENT

[program:celery]
directory = /home/dev/xxxx/
command = /home/dev/xxxx-env/bin/celery -A xxxx_freedata_django worker -B -l info
loglevel=INFO
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/long.err.log
stdout_logfile=/var/log/long.out.log

-celerybeat config file LOCAL ENVIRONMENT
sudo nano  /etc/supervisor/conf.d/celerybeat.conf

[program:celerybeat]
command=/home/USER/Desktop/xxxx/xxxx-env/bin/celery -A xxxx_freedata_django beat -l info
directory=/home/USER/Desktop/xxxx/xxxx/
user=root
numprocs=1
stdout_logfile=/var/log/stout_beat.log
stderr_logfile=/var/log/sterr_beat.log
autostart=true
autorestart=true

-celerybeat config file PRODUCTION ENVIRONMENT
sudo nano  /etc/supervisor/conf.d/celerybeat.conf

[program:celerybeat]
command=/home/dev/xxxx-env/bin/celery -A xxxx_freedata_django beat -l info
directory=/home/dev/xxxx/
user=root
numprocs=1
stdout_logfile=/var/log/stout_beat.log
stderr_logfile=/var/log/sterr_beat.log
autostart=true
autorestart=true


-creationg log files
sudo touch /var/log/stout_beat.log
sudo touch /var/log/sterr_beat.log
sudo touch /var/log/stout_beat.log
sudo touch /var/log/sterr_beat.log



-running the file
-reread the contents of the file whenever it changes and updates
sudo supervisorctl reread
sudo supervisorctl update

-check running activities and get interactive console
sudo supervisorctl 

-on console, you can run
supervisor> stop celery
supervisor> start celery
supervisor> restart celery

-Using the tail command, we can view the most recent entries in the stdout and stderr logs for our  program: from console
tail celery
tail celery stderr

-Using status we can view again the current execution state of each program after making any changes:
status


-check logs 
sudo tail /var/log/long.out.log
sudo tail /var/log/long.err.log
sudo tail /var/log/stout_beat.log
sudo tail /var/log/sterr_beat.log

-----------------------------------------------------------

REDIS

-logs
/var/log/redis/redis-server.log

-running
redis-server

-stop server, fix port duplication problems at times
sudo service redis-server stop

-start
sudo service redis-server start 

-all
sudo service redis-server  {start|stop|restart|force-reload|status}

----------------------------------------------------------
ADDITIONAL LINUX COMMANDS

-copy a .env fle to /wmecreativesnew/wmecreativesnew folder on the server
scp .env wiz@{SERVER IP}:~/wmecreativesnew/wmecreativesnew

-config file is in /etc/












fix secret key issue
import os
import json
with open('/etc/wmecreativesconfig.json') as config_file:
    config = json.load(config_file)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if config["PRODUCTION"] == "No":
    DEBUG = True
else:
    DEBUG = False
