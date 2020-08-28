from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="category-list")
router.register(r'products', ProductViewSet, basename="products-list")

urlpatterns = router.urls
