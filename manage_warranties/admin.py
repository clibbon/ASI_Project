from django.contrib import admin
from manage_warranties.models import (Customers, Products, ProductSellers, 
                                      ProductModels,Importers,Warranties,
                                      MessageHistory)

# Define field views
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','mob_number','past_messages')
    fieldsets = [
        ('Name',      {'fields':
                     ['first_name','last_name']}),
        ('Details', {'fields':
                     ['mob_number','region','cust_test']})
                 ]
                 

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('model','mid', 'is_verified')
    
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('cid','reg_date','exp_date', 'customer_name')
    list_filter = ['reg_date']

class MessageAdmin(admin.ModelAdmin):
    list_display = ('date_received', 'mob_number', 'msg_text')
    list_filter = ['date_received']

# Register your models here.
admin.site.register(Customers, CustomerAdmin)
admin.site.register(Products)
admin.site.register(ProductSellers)
admin.site.register(ProductModels, ProductModelAdmin)
admin.site.register(Importers)
admin.site.register(Warranties, WarrantyAdmin)
admin.site.register(MessageHistory, MessageAdmin)

