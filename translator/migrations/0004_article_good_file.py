# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0003_article_article_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='good_file',
            field=models.BooleanField(default=True),
        ),
    ]
