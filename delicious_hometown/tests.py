from django.test import TestCase

# Create your tests here.
import os
import random
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_demo.settings")  # 这里需要注意：1.MODULE； 2.django-project.settings
import django
django.setup()
from delicious_hometown import models

a = 'adfs'

if int(a):
    print('123')
else:
    print('243')



