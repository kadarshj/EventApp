# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-17 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_bookdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetails',
            name='txnid',
            field=models.CharField(default='', max_length=75),
        ),
    ]