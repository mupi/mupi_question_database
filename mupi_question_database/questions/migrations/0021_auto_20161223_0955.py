# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-23 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0020_auto_20161223_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_list',
            name='questions',
            field=models.ManyToManyField(through='questions.QuestionQuestion_List', to='questions.Question'),
        ),
    ]
