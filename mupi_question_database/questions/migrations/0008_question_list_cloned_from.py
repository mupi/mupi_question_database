# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-21 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_question_list_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_list',
            name='cloned_from',
            field=models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subarticles', to='questions.Question_List'),
        ),
    ]