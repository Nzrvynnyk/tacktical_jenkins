FROM python:3.9

WORKDIR /app
RUN apt-get update && apt-get install -y git 
RUN git clone https://github.com/Nzrvynnyk/tacktical_jenkins.git .

RUN pip install -r requirements.txt

