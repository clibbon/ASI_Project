# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_warranties', '0003_auto_20150330_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodels',
            name='is_verified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
