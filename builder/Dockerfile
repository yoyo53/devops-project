FROM node:slim

RUN apt-get update && apt-get install -y software-properties-common python3-launchpadlib python3-dotenv python3-discord
RUN add-apt-repository -y ppa:ansible/ansible
RUN apt-get update && apt-get install -y ansible

ADD ./discord-bot.py /discord-bot.py
RUN chmod +x /discord-bot.py

RUN mkdir -p ~/.ssh
