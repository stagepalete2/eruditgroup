# Generated by Django 5.1 on 2024-10-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eruditplatform', '0034_rename_assignemnts_note_groupassignment_assignemnt_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupassignment',
            name='assignment_attachments',
            field=models.ManyToManyField(blank=True, to='eruditplatform.assignmentattachments'),
        ),
    ]
