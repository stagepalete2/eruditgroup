# Generated by Django 5.1 on 2024-09-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.SlugField(default=''),
        ),
    ]
