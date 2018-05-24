FROM ubuntu
#ADD . /code
#WORKDIR /code
run apt-get update
run apt-get install gcc -y
run apt-get install python3 python3-pip -y
#RUN pip3 install -r requirements.txt
