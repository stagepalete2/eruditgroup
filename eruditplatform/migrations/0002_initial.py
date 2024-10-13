# Generated by Django 5.1 on 2024-10-09 00:07

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eruditplatform', '0001_initial'),
        ('school', '0001_initial'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentgrade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courseassignment',
            name='assignment_attachments',
            field=models.ManyToManyField(blank=True, to='eruditplatform.assignmentattachments'),
        ),
        migrations.AddField(
            model_name='courseassignment',
            name='assignment_grades',
            field=models.ManyToManyField(blank=True, to='eruditplatform.assignmentgrade'),
        ),
        migrations.AddField(
            model_name='courseassignment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignmentgrade',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eruditplatform.courseassignment'),
        ),
        migrations.AddField(
            model_name='courselesson',
            name='assignments',
            field=models.ManyToManyField(blank=True, to='eruditplatform.courseassignment'),
        ),
        migrations.AddField(
            model_name='courselesson',
            name='lesson_attachments',
            field=models.ManyToManyField(blank=True, to='eruditplatform.assignmentattachments'),
        ),
        migrations.AddField(
            model_name='groupattendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.course'),
        ),
        migrations.AddField(
            model_name='groupcourse',
            name='group_attendence',
            field=models.ManyToManyField(blank=True, to='eruditplatform.groupattendance'),
        ),
        migrations.AddField(
            model_name='groupcourse',
            name='group_grade',
            field=models.ManyToManyField(blank=True, to='eruditplatform.assignmentgrade'),
        ),
        migrations.AddField(
            model_name='groupcourse',
            name='group_lesson',
            field=models.ManyToManyField(blank=True, to='eruditplatform.courselesson'),
        ),
        migrations.AddField(
            model_name='groupcourse',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groups',
            name='group_participants',
            field=models.ManyToManyField(related_name='GroupParticipants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupcourse',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eruditplatform.groups'),
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='hotlink',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eruditplatform.news'),
        ),
        migrations.AddField(
            model_name='groupcourse',
            name='time_table',
            field=models.ManyToManyField(to='eruditplatform.timetable'),
        ),
    ]
