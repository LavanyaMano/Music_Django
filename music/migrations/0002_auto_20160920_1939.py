# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='artist',
            new_name='artists',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='genre',
            new_name='genres',
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.RemoveField(
            model_name='track',
            name='rating',
        ),
        migrations.AddField(
            model_name='album',
            name='tracks',
            field=models.ManyToManyField(to='music.Track', blank=True),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
