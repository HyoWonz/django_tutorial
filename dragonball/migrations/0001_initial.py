# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-24 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dragonball',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dragonball', models.CharField(max_length=5)),
                ('detected', models.CharField(max_length=10)),
            ],
        ),
    ]
