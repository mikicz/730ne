# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-17 14:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('signed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]