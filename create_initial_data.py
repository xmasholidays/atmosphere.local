import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmasatm.settings")
django.setup()

from django.contrib.auth.models import User
superuser_exists = User.objects.filter(username='admin').exists()
if superuser_exists:
    print ('Superuser already exists')
else:
    print ('Superuser does not exists. Creating..')
    user = User.objects.create_user('admin', password='admin')
    user.is_superuser = True
    user.is_staff = True
    user.save()