# Generated by Django 5.1 on 2024-09-25 06:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_article_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_body',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
