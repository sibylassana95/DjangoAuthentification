import os
import subprocess

# Activer l'environnement virtuel
subprocess.run(['workon', 'venv'], shell=True)

# Se déplacer dans le répertoire DjangoAuthentification
os.chdir('/home/djangoauth/DjangoAuthentification')

# Exécuter les commandes Django
subprocess.run(['python', 'manage.py', 'makemigrations'])
subprocess.run(['python', 'manage.py', 'migrate'])
subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput'])