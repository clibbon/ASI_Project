# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_warranties', '0004_auto_20150330_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('msg_text', models.CharField(max_length=450)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
