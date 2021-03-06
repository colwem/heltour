# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-03 19:03


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0131_registration_validation_warning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playernotificationsetting',
            name='type',
            field=models.CharField(choices=[('round_started', 'Round started'), ('before_game_time', 'Before game time'), ('game_time', 'Game time'), ('unscheduled_game', 'Unscheduled game'), ('game_warning', 'Game warning'), ('alternate_needed', 'Alternate needed')], max_length=255),
        ),
    ]
