FROM gitlab/gitlab-ee:latest

RUN mkdir -p /app/project
WORKDIR /app/project

RUN git clone https://github.com/facebook/create-react-app.git .
ADD .gitlab-ci.yml .
ADD deploy-playbook.yaml .
ADD inventory.ini .

RUN git config --global user.email "root@root.com"
RUN git config --global user.name "root"
