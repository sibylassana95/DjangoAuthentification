#!/bin/bash

# Activer l'environnement virtuel
source /home/${PA_USERNAME}/.virtualenvs/venv/bin/activate

# Se déplacer dans le répertoire DjangoAuthentification
cd /home/${PA_USERNAME}/DjangoAuthentification

# Exécuter les commandes Django
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

# Redémarrer l'application web
curl -X POST -H "Authorization: Token ${PA_API_TOKEN}" \
  https://www.pythonanywhere.com/api/v0/user/${PA_USERNAME}/webapps/${PA_USERNAME}.pythonanywhere.com/reload/