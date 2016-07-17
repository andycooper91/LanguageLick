# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_name', models.CharField(max_length=50)),
                ('language_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phrase', models.CharField(max_length=200)),
                ('language', models.ForeignKey(to='translator.Language')),
            ],
        ),
        migrations.CreateModel(
            name='PhraseSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('translation_date', models.DateTimeField(verbose_name=b'date published')),
                ('from_phrase', models.ForeignKey(related_name='from_phrase', to='translator.Phrase')),
                ('to_phrase', models.ForeignKey(related_name='to_phrase', to='translator.Phrase')),
            ],
        ),
        migrations.AddField(
            model_name='phrase',
            name='source',
            field=models.ForeignKey(to='translator.PhraseSource'),
        ),
    ]
