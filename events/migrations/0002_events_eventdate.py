# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-16 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='eventdate',
            field=models.DateField(default=None),
        ),
    ]