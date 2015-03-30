# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('cid', models.IntegerField(serialize=False, primary_key=True, db_column='cID')),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('mob_number', models.CharField(max_length=12, blank=True)),
                ('region', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'customers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Importers',
            fields=[
                ('iid', models.IntegerField(serialize=False, primary_key=True, db_column='iID')),
                ('identity', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'db_table': 'importers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductModels',
            fields=[
                ('mid', models.IntegerField(serialize=False, primary_key=True, db_column='mID')),
                ('model', models.CharField(max_length=20, blank=True)),
                ('is_verified', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'product_models',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pid', models.IntegerField(serialize=False, primary_key=True, db_column='pID')),
                ('ser_num', models.CharField(max_length=30, blank=True)),
                ('model', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'db_table': 'products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductSellers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iid', models.IntegerField(db_column='iID')),
                ('pid', models.IntegerField(db_column='pID')),
                ('imp_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'product_sellers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Warranties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.IntegerField(db_column='cID')),
                ('pid', models.IntegerField(db_column='pID')),
                ('ser_num', models.CharField(max_length=30, blank=True)),
                ('reg_date', models.DateField(null=True, blank=True)),
                ('exp_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'warranties',
            },
            bases=(models.Model,),
        ),
    ]
