# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=20)),
                ('stream_key', models.CharField(max_length=32)),
                ('date created', models.DateTimeField(auto_now_add=True)),
                ('is_private', models.BooleanField(default=False)),
            ],
        ),
    ]
