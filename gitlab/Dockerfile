FROM gitlab/gitlab-ee:latest

RUN mkdir -p /app/tp1
WORKDIR /app/tp1

RUN git clone https://github.com/facebook/create-react-app.git .
ADD .gitlab-ci.yml .
ADD deploy-playbook.yaml .
ADD inventory.ini .

RUN git config --global user.email "root@root.com"
RUN git config --global user.name "root"
