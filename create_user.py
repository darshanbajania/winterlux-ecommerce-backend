import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings')
django.setup()

User = get_user_model()
username = 'testuser'
email = 'user@example.com'
password = 'password'

if not User.objects.filter(username=username).exists():
    User.objects.create_user(username, email, password)
    print(f'User "{username}" created.')
else:
    print(f'User "{username}" already exists.')
