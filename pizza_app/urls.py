from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductView

router = DefaultRouter()
router.register(r'projects', ProductView)

urlpatterns = []

urlpatterns += router.urls