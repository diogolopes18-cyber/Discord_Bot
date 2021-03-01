FROM python:3.7.9-stretch

RUN apt-get update && apt-get install -y \
    software-properties-common \
    apache2 \
    curl \
    python3-pip

#Install pip
RUN pip install --upgrade pip
WORKDIR /home/bot
COPY ./requirements.txt /home/bot/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./bot-docker.py /home/bot/bot.py

CMD [ "/bin/bash","-c","python3 /home/bot/bot.py" ]