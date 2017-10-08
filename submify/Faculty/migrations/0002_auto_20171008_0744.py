# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 07:44
from __future__ import unicode_literals

import Faculty.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='lateSubmissionPeriod',
            field=models.IntegerField(blank=True, null=True, validators=[Faculty.models.validate_late_submission], verbose_name='Late submission period (in minutes)'),
        ),
    ]
