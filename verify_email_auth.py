import os
import django
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings')
django.setup()

User = get_user_model()
username = 'test_email_user'
email = 'emailtest@example.com'
password = 'password'

# Ensure user exists
if not User.objects.filter(username=username).exists():
    User.objects.create_user(username, email, password)
    print(f'User "{username}" created with email "{email}".')

# Try authenticating with email
user = authenticate(username=email, password=password)
if user:
    print(f"Authentication successful for email: {email}")
else:
    print(f"Authentication FAILED for email: {email}")

# Try authenticating with username (should still work if backend supports it or logic covers it)
user_username = authenticate(username=username, password=password)
if user_username:
    print(f"Authentication successful for username: {username}")
else:
    print(f"Authentication FAILED for username: {username}")
