from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductView, SupplierView

router = DefaultRouter()
router.register(r'products', ProductView)
router.register(r'suppliers', SupplierView)

urlpatterns = []

urlpatterns += router.urls