# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_warranties', '0004_auto_20150330_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsellers',
            name='id',
        ),
        migrations.RemoveField(
            model_name='warranties',
            name='id',
        ),
    ]
