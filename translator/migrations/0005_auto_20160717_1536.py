# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0004_article_good_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='file_name',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
