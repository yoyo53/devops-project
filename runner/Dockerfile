FROM gitlab/gitlab-runner:latest

RUN curl -fsSL https://get.docker.com | bash 
RUN apt-get update && apt-get install -y containerd docker.io vim

RUN mkdir -p ~/.ssh
