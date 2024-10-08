# Generated by Django 5.1 on 2024-09-24 22:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_course_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_main_image',
            field=models.ImageField(blank=True, upload_to='course_images/main_images/'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_sub_image',
            field=models.ImageField(blank=True, upload_to='course_images/sub_images/'),
        ),
    ]
