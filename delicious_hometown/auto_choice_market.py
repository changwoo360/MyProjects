from django.test import TestCase
# 每天0点运行一次该脚本


# Create your tests here.
import os
import random
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_demo.settings")  # 这里需要注意：1.MODULE； 2.django-project.settings
import django
django.setup()
from delicious_hometown import models

models.ChoiceMarket.objects.filter(test=1).all().delete()

choice_list = random.sample([i.pk for i in models.FoodMaterial.objects.all()], 3)
for choice in choice_list:
    models.ChoiceMarket(test=1, market_material_id=choice).save()

