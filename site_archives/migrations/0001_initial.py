# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_url', models.URLField(max_length=400)),
                ('new_url', models.URLField(max_length=400)),
                ('archive_online', models.BooleanField()),
                ('short_desc', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
    ]
