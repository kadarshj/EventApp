# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-17 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_bookdetails_txnid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='booked_seats',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
