# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-17 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180317_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('coupon_code', models.CharField(max_length=5)),
                ('discount_percent', models.IntegerField(default=0)),
                ('is_activated', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Events')),
            ],
        ),
    ]
