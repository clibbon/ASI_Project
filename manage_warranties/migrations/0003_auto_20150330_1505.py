# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_warranties', '0002_auto_20150330_1442'),
    ]

    operations = [

        migrations.AlterField(
            model_name='productsellers',
            name='pid',
            field=models.IntegerField(serialize=False, primary_key=True, db_column='pID'),
            preserve_default=True,
        ),
    ]
