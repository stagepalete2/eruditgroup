# Generated by Django 5.1 on 2024-09-26 22:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_phone_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_child',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
