from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Supplier, Product, Pizzaplace, Warehouse, WarehouseProduct, Order, OrderProduct, Sale, SaleProduct, Notification
from .serializers import ProductSerializer, SupplierSerializer, PizzaplaceSerializer, OrderProductSerializer, NotificationSerializer, OrderSerializer, WarehouseProductSerializer, WarehouseSerializer, SaleProductSerializer, SaleSerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['price', 'id', 'category', 'supplier']
    search_fields = ['name', 'category']

class SupplierView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer