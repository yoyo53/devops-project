FROM nginx:latest

RUN apt-get update && apt-get install python3 openssh-server -y
RUN mkdir -p ~/.ssh

ADD start.sh /docker-entrypoint.d/start-ssh.sh
RUN chmod 777 /docker-entrypoint.d/start-ssh.sh
