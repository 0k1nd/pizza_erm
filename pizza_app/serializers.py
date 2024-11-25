from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Supplier, Product, Pizzaplace, Warehouse, WarehouseProduct, Order, OrderProduct, Sale, SaleProduct, Notification

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class PizzaplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzaplace
        fields = '__all__'

class OrderProductSerializer(ModelSerializer):
    product_order = ProductSerializer(many=True)

    class Meta:
        model = OrderProduct
        fields = '__all__'

    def get_product_warehouse(self):
        return Product.objects.filter(product_order=model.id)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_product = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_order_product(self):
        return Order.objects.filter(order_product=model.id)




class WarehouseProductSerializer(ModelSerializer):
    product_warehouse = ProductSerializer(many=True)

    class Meta:
        model = WarehouseProduct
        fields = '__all__'

    def get_product_warehouse(self):
        return Product.objects.filter(product_warehouse=model.id)


class WarehouseSerializer(serializers.ModelSerializer):
    warehouse_product = WarehouseProductSerializer(many=True)

    class Meta:
        model = Warehouse
        fields = '__all__'

    def get_product_warehouse(self):
        return Warehouse.objects.filter(warehouse_product=model.id)

class SaleProductSerializer(ModelSerializer):
    product_sale = ProductSerializer(many=True)

    class Meta:
        model = SaleProduct
        fields = '__all__'

    def get_product_warehouse(self):
        return Product.objects.filter(product_sale=model.id)

class SaleSerializer(serializers.ModelSerializer):
    sale_product = SaleProductSerializer(many=True)

    class Meta:
        model = Sale
        fields = '__all__'

    def get_sale_product(self):
        return Sale.objects.filter(sale_product=model.id)
