# Generated by Django 5.0.1 on 2024-01-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='createAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('isActive', models.BooleanField(default=True)),
                ('isStaff', models.BooleanField(default=False)),
                ('surname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('birthDate', models.DateTimeField(max_length=255)),
                ('paymentMethod', models.CharField(max_length=255)),
            ],
        ),
    ]
