# Generated by Django 5.1 on 2024-09-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
