# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Customers(models.Model):
    cid = models.AutoField(primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    mob_number = models.CharField(max_length=24, blank=True)
    region = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        db_table = 'customers'
        verbose_name_plural = 'customers'

class Importers(models.Model):
    iid = models.AutoField(primary_key=True)  # Field name made lowercase.
    identity = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = 'importers'
        verbose_name_plural = 'importers'

class ProductModels(models.Model):
    mid = models.AutoField(primary_key=True)  # Field name made lowercase.
    model = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_models'
        verbose_name_plural = 'product_models'


class ProductSellers(models.Model):
    iid = models.IntegerField()  # Field name made lowercase.
    pid = models.AutoField(primary_key=True)  # Field name made lowercase.
    imp_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'product_sellers'
        verbose_name_plural = 'product_sellers'


class Products(models.Model):
    pid = models.AutoField(primary_key=True)  # Field name made lowercase.
    ser_num = models.CharField(max_length=30, blank=True)
    model = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'products'
        verbose_name_plural = 'products'


class Warranties(models.Model):
    cid = models.IntegerField()  # Field name made lowercase.
    pid = models.AutoField(primary_key=True)  # Field name made lowercase.
    ser_num = models.CharField(max_length=30, blank=True)
    reg_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'warranties'
        verbose_name_plural = 'warranties'


class MessageHistory(models.Model):
    id = models.AutoField(primary_key=True)
    msg_text = models.CharField(max_length=450)
    date_received = models.DateField(blank=True, null=True)
    mob_number = models.CharField(max_length=24, blank=True)
    
    class Meta:
        db_table = 'msg_history'
        verbose_name_plural = 'msg_history'


