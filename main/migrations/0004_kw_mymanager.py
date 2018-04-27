# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-27 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_mymanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('num', models.IntegerField()),
                ('buk', models.CharField(max_length=5)),
                ('prim', models.CharField(max_length=100)),
                ('kw_dom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Dom')),
            ],
            options={
                'verbose_name_plural': 'kws',
                'ordering': ['num', 'buk'],
            },
        ),
        migrations.CreateModel(
            name='MyManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]