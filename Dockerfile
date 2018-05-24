FROM ubuntu
#ADD . /code
#WORKDIR /code
RUN apt-get update
RUN apt-get install gcc -y
RUN apt-get install python3 python3-pip -y
#RUN pip3 install -r requirements.txt
