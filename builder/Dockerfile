FROM node:slim

RUN apt-get update && apt-get install -y software-properties-common python3-launchpadlib
RUN add-apt-repository -y ppa:ansible/ansible
RUN apt-get update && apt-get install -y ansible

RUN mkdir -p ~/.ssh
