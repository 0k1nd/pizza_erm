from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Supplier, Product, Pizzaplace, Warehouse, WarehouseProduct

@admin.register(Supplier)
class SupplierAdmin(ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass

@admin.register(Pizzaplace)
class PizzaplaceAdmin(ModelAdmin):
    pass

@admin.register(Warehouse)
class WarehouseAdmin(ModelAdmin):
    pass

@admin.register(WarehouseProduct)
class WarehouseProductAdmin(ModelAdmin):
    pass


# Register your models here.
