# Système d'Authentification Django

Un système d'authentification complet développé avec Django, incluant l'inscription, la connexion, la déconnexion et la réinitialisation de mot de passe.

## Fonctionnalités

- 👤 Inscription utilisateur avec validation
- 🔐 Connexion/Déconnexion
- 📧 Réinitialisation de mot de passe par email
- 🌓 Mode sombre/clair
- 🎨 Interface utilisateur moderne avec Tailwind CSS
- 📱 Design responsive
- 🔒 Sécurité renforcée

## Technologies Utilisées

- Django 5.0.7
- Tailwind CSS
- Flowbite
- SQLite3
- JavaScript

## Configuration Requise

- Python 3.8+
- pip

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/sibylassana95/DjangoAuthentification.git
cd DjangoAuthentification
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Effectuez les migrations :
```bash
python manage.py migrate
```

5. Créez un super utilisateur :
```bash
python manage.py createsuperuser
```

6. Configurez les variables d'environnement pour l'email et la base de donnée dans `settings.py` :
```python
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
```
```python
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
    }
```
7. Lancez le serveur :
```bash
python manage.py runserver
```

## Structure du Projet

```
DjangoAuthentification/

├── accounts/                 # Application principale
│   ├── migrations/          # Migrations de base de données
│   ├── templates/           # Templates HTML
│   ├── admin.py            # Configuration admin
│   ├── models.py           # Modèles de données
│   ├── urls.py             # Configuration des URLs
│   └── views.py            # Logique des vues
├── AuthenticationProject/    # Configuration du projet
├── static/                  # Fichiers statiques
├── templates/              # Templates globaux
├── manage.py               
└── README.md               # Readme du projet
└── LICENSE                 # Licence du projet

```

## Fonctionnalités Détaillées

### Inscription
- Validation des champs requis
- Vérification d'unicité du nom d'utilisateur et de l'email
- Validation de la force du mot de passe

### Connexion
- Authentification sécurisée
- Protection contre les tentatives de connexion multiples
- Sessions utilisateur

### Réinitialisation de Mot de Passe
- Envoi d'email sécurisé
- Lien de réinitialisation unique
- Expiration du lien après 10 minutes
- Double validation du nouveau mot de passe

## Sécurité

- Protection CSRF
- Hachage des mots de passe
- Validation des données
- Sessions sécurisées
- Protection contre les injections SQL

## Personnalisation de l'Interface

L'interface utilise Tailwind CSS pour un design moderne et responsive. Le mode sombre est disponible et peut être activé via le bouton dans la barre de navigation.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

## 👤 Auteur 

[![LASSANA SIBY](https://avatars.githubusercontent.com/u/103085452?u=13ace4d88a52056741734e0f802ca7c0053e1e80&v=4&s=40)](https://github.com/sibylassana95)  
Created by **[Lassana SIBY](https://github.com/sibylassana95)**

