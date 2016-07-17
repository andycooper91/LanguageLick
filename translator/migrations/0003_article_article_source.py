# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_source',
            field=models.CharField(default='yahoo_deportes', max_length=200),
            preserve_default=False,
        ),
    ]
