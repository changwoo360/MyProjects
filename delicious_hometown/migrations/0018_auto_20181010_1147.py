# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-10 03:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delicious_hometown', '0017_auto_20181010_1144'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RestaurantRecipe',
            new_name='UserRecipe',
        ),
    ]