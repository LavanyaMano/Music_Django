# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20160920_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('category', models.CharField(max_length=10, default='audio', choices=[('audio', 'Audio'), ('video', 'Video')])),
            ],
        ),
        migrations.AlterField(
            model_name='track',
            name='artists',
            field=models.ManyToManyField(to='music.Artist', blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='track_type',
            field=models.ManyToManyField(to='music.TrackType'),
        ),
    ]
