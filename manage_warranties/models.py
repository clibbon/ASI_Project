from django.db import models

# Customer
class Customer(models.Model):
    cId = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mob_number = models.CharField(max_length=11)
    region = models.IntegerField(defaul=0)

# Importer
class Importer(models.Model):
    iId = models.IntegerField(primary_key=True)

# Model
class Product_Model(models.Model):
    mId = models.IntegerField(primary_key=True)
    verified = models.BooleanField(defaul=False)



# Warranty 

# Individual product
class Product(models.Model):
    serNum = models.CharField(max_length=20) # Not unique as only unique with model number
    pId = models.IntegerField(primary_key=True)
    mId = models.ForeignKey(Product_Model)
    
# Product Seller
class Product_Seller(models.Model):
    iId = models.ForeignKey(Importer)
    pId = models.ForeignKey(Product)
    regId =s    
    