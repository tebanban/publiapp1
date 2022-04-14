# Back End

How to start

# 1 Create virtual Enviroment
pipenv shell

# 2 install dependencies 
pipenv install

# 3 Migrate migrations 
pipenv run init
pipenv run migrate   (skip if you have not made changes to the models on the `./src/api/models.py`)
pipenv run upgrade

# 4 Run app
pipenv run start


# To modify URL at .env
mysql url: mysql://puadmin:*****@mysql.nuevo.publiexcr.com/sisvallas21

# To install Mysql module: 
 pip install mysqlclient

# Flask Error: Target database is not up to date.
flask db stamp head

# dreamhost
 Connect to your new database from the command line with:
 
# Gitpod greenlet error
pip install greenlet

# npm ERR!
nvm install v14.18.1 
nvm use v14.18.1  ( optional)
npm install

# psql FATAL password authentication failed for user "postgres" 
psql -U default (terminal)
\password  (psql shell)
Enter new password:

# Install PostgreSQL on WSL (ubuntu)
https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-database