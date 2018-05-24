# Sentiment Analysis


## To install manually

- Create mysql database and give permissions

      $ mysql -u root -p
      > create database octopus;
      > GRANT ALL PRIVILEGES ON octopus.* TO 'octotest'@'localhost' IDENTIFIED BY 'Q1x2v4c5';

- Be sure to change settings.py database settings to meet your localhost mysql database and user
- In project folder install requirements. It is suggested to use virtual environment

       $ pip3 install -r requirements.txt

- run the server

      $ python3 main.py

- access it from http://localhost:8888

## To run it on docker. 

- install docker and docker compose
- Run the command below in project folder

      $ docker-compose up

- access it from http://localhost:8888

## To secure the private key file 

- the key files are generated when you first run the code
- change its permissions

      $ chmod 400 privatekey

- be aware that changing or deleting key files makes database data unusable. Be sure to take backup of your database with key files

