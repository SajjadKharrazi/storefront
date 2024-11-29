from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views

# URLConf
router = DefaultRouter()
router.register('products', views.ProductViewSet)
urlpatterns = router.urls
