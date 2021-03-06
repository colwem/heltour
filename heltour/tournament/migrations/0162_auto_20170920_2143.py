# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-20 21:43


from django.db import migrations
import django.db.models.deletion
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0161_logintoken_username_hint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slackaccount',
            name='lichess_username',
        ),
        migrations.AddField(
            model_name='slackaccount',
            name='player',
            field=select2.fields.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='tournament.Player'),
            preserve_default=False,
        ),
    ]
