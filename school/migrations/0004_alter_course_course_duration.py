# Generated by Django 5.1 on 2024-09-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_course_course_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_duration',
            field=models.DurationField(default='01:00:00', null=True),
        ),
    ]
