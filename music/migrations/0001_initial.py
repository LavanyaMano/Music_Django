# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('category', models.CharField(max_length=50, default='others', choices=[('african', 'African'), ('asian', 'Asian'), ('blues', 'Blues'), ('caribbean', 'Caribbean'), ('comedy', 'Comedy'), ('country', 'Country'), ('electronic', 'Electronic'), ('folk', 'Folk'), ('hiphop', 'Hiphop'), ('jazz', 'Jazz'), ('latin', 'Latin'), ('pop', 'Pop'), ('rock', 'Rock'), ('others', 'Others')])),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('album', models.ForeignKey(to='music.Album')),
                ('artist', models.ManyToManyField(to='music.Artist')),
                ('genre', models.ManyToManyField(to='music.Genre')),
                ('rating', models.ManyToManyField(to='music.Rating')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
