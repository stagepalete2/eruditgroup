# Generated by Django 5.1 on 2024-09-24 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_coursecategory_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_slug',
            field=models.SlugField(default=''),
        ),
    ]
