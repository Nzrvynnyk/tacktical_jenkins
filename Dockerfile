FROM python:3.9

WORKDIR /app
RUN apt-get update && apt-get install -y git 
RUN git clone https://github.com/Nzrvynnyk/tacktical_jenkins.git /app/.
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]