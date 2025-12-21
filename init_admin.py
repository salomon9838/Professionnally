import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'propri.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='salomon').exists():
    User.objects.create_superuser('salomon', 'votre@email.com', 'VotreMotDePasse123')
    print("Superutilisateur créé !")
