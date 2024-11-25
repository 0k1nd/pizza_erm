from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Supplier, Product, Pizzaplace, Warehouse, WarehouseProduct, Order, OrderProduct, Sale, SaleProduct

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

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass

@admin.register(OrderProduct)
class OrderProductAdmin(ModelAdmin):
    pass

@admin.register(Sale)
class SaleAdmin(ModelAdmin):
    pass

@admin.register(SaleProduct)
class SaleProductAdmin(ModelAdmin):
    pass
# Register your models here.
