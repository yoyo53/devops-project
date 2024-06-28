# devops-project

## Installation
1. extraire le zip et lancer les docker
```bash
sudo docker compose build
sudo docker compose up -d gitlab gitlab-runner web-server
```

2. attendre que gitlab ai fini de boot (voir http://localhost/)

3. se connecter au conteneur gitlab et push le projet
```bash
sudo docker exec -it gitlab bash
```
```bash
GITLAB_PWD=$(cat /etc/gitlab/initial_root_password | grep Password: | awk '{print $2}')
GITLAB_PWD_ENCODED=$(python3 -c "import urllib.parse; print(urllib.parse.quote('''$GITLAB_PWD''', 'urlencode_safe'))")
git init --initial-branch=main
git remote set-url origin http://root:${GITLAB_PWD_ENCODED}@localhost/root/devops-project.git
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
echo $GITLAB_PWD
```

4. se connecter au conteneur gitlab-runner et générer une clé RSA
```bash
sudo docker exec -it gitlab-runner bash
```
```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -P ""
cat ~/.ssh/id_rsa.pub | docker exec -i web-server bash -c 'cat >> ~/.ssh/authorized_keys'
cat ~/.ssh/id_rsa | base64 -w0; echo 
```
ça affiche la clé privée encodée en base 64, la copier pour l'étape suivante

5. enregistrer la clé privée RSA comme variable d'environnement du projet gitlab depuis l'interface web
  - Settings -> CI/CD -> Variables -> Add variable
  - choisir 'masked' dans Visibility
  - décocher les flags 'Protect variable' et 'Expand variable reference'
  - mettre 'SSH_PRIVATE_KEY' comme key
  - mettre la clé privée copiée à l'étape d'avant comme value

6. créer un bot discord depuis le portail développeur (https://discord.com/developers)
  - New application -> Create
  - OAuth2 -> cocher 'bot' dans OAuth2 URL Generator -> cocher 'Send Messages' dans BOT PERMISSIONS
  - ouvrir l'url généré et ajouter le bot à un serveur
  - copier le token du bot (Bot -> TOKEN -> Reset Token -> Yes -> Copy)
  - ajouter le token du bot en variable d'environnement gitlab avec DISCORD_TOKEN comme clé (cf partie 5)
  - depuis discord, copier l'id du salon où les notifications seront envoyées (clic droit -> copier l'identifiant du salon)
  - ajouter l'id du salon en variable d'environnement gitlab avec DISCORD_CHANNEL comme clé (cf partie 5)

7. créer un nouveau runner depuis l'interface web
  - Settings -> CI/CD -> Runners -> New project runner
  - cocher 'Run untagged jobs' puis create runner
  - ca marche pas c'est normal : changer l'url de gitlab en localhost
  - copier le token pour le runner

8. register le runner depuis le conteneur gitlab-runner
```bash
gitlab-runner register
```
Laisser tout par defaut en insérant votre token

9. attendre que la pipeline soit finie d'exécuter et aller sur http://localhost:8080/ pour voir le projet