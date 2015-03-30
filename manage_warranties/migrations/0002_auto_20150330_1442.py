# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_warranties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranties',
            name='pid',
            field=models.IntegerField(serialize=False, primary_key=True, db_column='pID'),
            preserve_default=True,
        ),
    ]
