from django.contrib import admin
from manage_warranties.models import (Customers, Products, ProductSellers, 
                                      ProductModels,Importers,Warranties,
                                      MessageHistory)

# Define field views
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',      {'fields':
                     ['first_name','last_name']}),
        ('Details', {'fields':
                     ['mob_number','region']})
                 ]

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('model','mid', 'is_verified')
    
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('cid','reg_date','exp_date')
    list_filter = ['exp_date']

class MessageAdmin(admin.ModelAdmin):
    list_display = ('date_received', )
    list_filter = ['date_received']

# Register your models here.
admin.site.register(Customers, CustomerAdmin)
admin.site.register(Products)
admin.site.register(ProductSellers)
admin.site.register(ProductModels, ProductModelAdmin)
admin.site.register(Importers)
admin.site.register(Warranties, WarrantyAdmin)
admin.site.register(MessageHistory, MessageAdmin)

