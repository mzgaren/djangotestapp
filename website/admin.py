from django.contrib import admin
from .models import Report, Customer, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'description')

# Register your models here.
admin.site.register(Report)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)