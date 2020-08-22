# base image
FROM python:3.8-slim

# install netcat
RUN apt-get update && apt-get clean
RUN apt-get install ffmpeg

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY lifebot.py /usr/src/app
COPY bot /usr/src/app/bot
COPY SmoothLife /usr/src/app/SmoothLife
COPY log /usr/src/app/log

# run server
CMD ["/usr/src/app/entrypoint.sh"]
