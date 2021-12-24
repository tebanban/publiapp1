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
mysql url: mysql://puadmin:*****@mysql.nuevo.publiexcr.com/sisvallas2021

# To install Mysql module: 
 pip install mysqlclient

 # dreamhost
 Connect to your new database from the command line with:
 mysql -u puadmin -p -h mysql.nuevo.publiexcr.com sisvallas21
 You can also go to http://mysql.nuevo.publiexcr.com/ to   manage your MySQL database from the web. 