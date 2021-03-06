# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-21 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=3, max_digits=4)),
                ('type', models.CharField(max_length=100)),
                ('product_image', models.CharField(max_length=1000)),
            ],
        ),
    ]
