# Generated by Django 5.1 on 2024-10-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eruditplatform', '0026_remove_groupcourse_group_assignments'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouplesson',
            name='lesson_title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
