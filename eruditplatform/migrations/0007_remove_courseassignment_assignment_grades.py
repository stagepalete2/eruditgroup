# Generated by Django 5.1 on 2024-10-13 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eruditplatform', '0006_groupattendance_remark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseassignment',
            name='assignment_grades',
        ),
    ]
