from django.contrib import admin
from manage_warranties.models import Customers, Products, ProductSellers, ProductModels,Importers,Warranties

# Define field views
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',      {'fields':
                     ['first_name','last_name']}),
        ('Details', {'fields':
                     ['cid','mob_number','region']})
                 ]

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('model','mid', 'is_verified')
    
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('cid','reg_date','exp_date')
    list_filter = ['exp_date']

# Register your models here.
admin.site.register(Customers, CustomerAdmin)
admin.site.register(Products)
admin.site.register(ProductSellers)
admin.site.register(ProductModels, ProductModelAdmin)
admin.site.register(Importers)
admin.site.register(Warranties, WarrantyAdmin)

