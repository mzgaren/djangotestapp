from django.contrib import admin
from .models import Report, Customer, Product

# Register your models here.
admin.site.register(Report)
admin.site.register(Customer)
admin.site.register(Product)