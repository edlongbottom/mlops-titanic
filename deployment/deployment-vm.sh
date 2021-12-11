# Shell script for deploying flask app to unix virtual machine
# (to be run on VM)

# git clone code
git clone https://github.com/edlongbottom/kaggle_titanic

# install python, pip and venv
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv

# create a python virtual environment and activate it
python3 -m venv kaggle_titanic/venv
cd kaggle_titanic/
source venv/bin/activate

# pip install dependency packages
pip install -r deployment/requirements.txt

# create config file for any sensitive information, filepaths or other env vars
sudo touch /etc/config.yaml
sudo nano /etc/config.yaml

# edit app local config.py file to pull values from /etc/config.yaml
# => none created for this project

# test application by running it and then send a request from another device
cd deployment
export FLASK_APP=api.py
flask api --host=0.0.0.0

## ADDITIONAL STEPS FOR PRODUCTION
# Nginx and gunicorn are required to handle requests from multiple sources / high traffic. 
# Nginx is the web server gateway. It handles static files (HTML/CSS) and passes requests to Gunicorn.  
# Gunicorn is battle-tested, reliable and scalable. It uses WSGI (protocol for communication between web server (Gunicorn) and application (flask)). It handles python code. 
# install nginx and gunicorn
cd 
sudo apt install nginx
pip install gunicorn

# remove default nginx config file and create own one (mlservice)
sudo rm /etc/nginx/sites-enabled/default
sudo nano /etc/nginx/sites-enabled/mlservice
# include port to listen on (80) and server name (linux VM IP)
# include location of static files for a web app
# include location => proxy_pass to localhost:8000 (forwards traffic to gunicorn)
# => include reference to proxy_params
# => include proxy_redirect off

# open up port on VM firewall to http (and disallow traffic to port 5000)
sudo ufw allow http/tcp
sudo ufw delete allow 5000
sudo ufw enable

# restart nginx server
sudo systemctl restart nginx

# run guincorn (with 3 workers)
# (no. of workers = 2 x num_cores + 1) where num_cores is number of cores on your machine. Run 'nproc - all' to find out. 
# within api.py we have app
cd kaggle_titanic/deployment
gunicorn -w 3 api:app

# use a supervisor to run app in background and monitor it
sudo apt install supervisor

# create config file for supervisor (mlservice.conf)
sudo nano /etc/supervisor/conf.d/mlservice.conf
# => include [program:flaskblog]
# => include directory=/path/to/kaggle_titanic/deployment
# => include command=/path/to/kaggle_titanic/venv/bin/gunicorn -w 3 api:app
# => include user=<user>
# => include autostart=true
# => include autorestart=true
# => include stopasgroup=true
# => include killasgroup=true
# => include stderr_logfile=/var/log/mlservice/mlservice.err.log
# => include stdout_logfile=/var/log/mlservice/mlservice.out.log

# create those log files
sudo mkdir -p /var/log/mlservice
sudo touch /var/log/mlservice/mlservice.err.log
sudo touch /var/log/mlservice/mlservice.out.log

# restart supervisor
sudo supervisorctl reload 

# amend nginx settings to change defaults (optional extra)
sudo nano /etc/nginx/nginx.conf
# => modify settings as required
