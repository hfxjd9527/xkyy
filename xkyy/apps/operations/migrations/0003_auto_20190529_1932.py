# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-05-29 19:32
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('operations', '0002_auto_20190529_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('text', models.TextField(verbose_name='评论')),
                ('comment_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='operations.Comment')),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('root', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_comment', to='operations.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'ordering': ['-comment_time'],
            },
        ),
        migrations.RemoveField(
            model_name='comments',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='reply_to',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='root',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
