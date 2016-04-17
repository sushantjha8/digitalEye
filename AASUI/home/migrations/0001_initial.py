# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-30 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('branch', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='imagedata',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
    ]
