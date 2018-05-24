# Sentiment Analysis

## Features 

This is a sample project with the features below:
- Using Tornado web server
- Using SQLAlchemy ORM
- Have a sngle page to submit a URL
- Makes sentiment analysis of the submitted URL by using wit.ai
- Also counts all the words after cleaning stop words with nltk library
- Displays a word cloud according to number of frequency for top 100 words
- The words are saved to database using asymmetrical encryption 
- The urls are also saved to database with sentiment result
- Has an admin page to display the words and urls in database
- In frontend uses Bootstrap4 
- For tables in admin page uses Datatables


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

