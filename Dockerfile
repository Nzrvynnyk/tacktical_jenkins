FROM python:3.9

WORKDIR /app
RUN apt-get update && apt-get install -y git 
RUN git clone https://github.com/Nzrvynnyk/tacktical_jenkins.git .
RUN pip install requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


