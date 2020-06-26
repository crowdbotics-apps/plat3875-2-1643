from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BuyerAddressViewSet

router = DefaultRouter()
router.register("buyeraddress", BuyerAddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
