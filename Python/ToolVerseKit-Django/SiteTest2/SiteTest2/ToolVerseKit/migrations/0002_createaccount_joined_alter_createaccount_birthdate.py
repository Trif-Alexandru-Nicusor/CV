# Generated by Django 5.0.1 on 2024-01-21 15:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToolVerseKit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createaccount',
            name='joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='createaccount',
            name='birthDate',
            field=models.DateField(max_length=255),
        ),
    ]
