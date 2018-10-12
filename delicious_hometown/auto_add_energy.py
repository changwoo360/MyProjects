from django.test import TestCase

# Create your tests here.
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_demo.settings")  # 这里需要注意：1.MODULE； 2.django-project.settings
import django
django.setup()
from delicious_hometown import models

while 1:
    import time
    # time.sleep(216)
    time.sleep(60)
    user_obj = models.User.objects.filter(pk=1).first()
    energy = user_obj.energy
    energy = energy + 1
    models.User.objects.filter(pk=user_obj.pk).update(energy=energy)











