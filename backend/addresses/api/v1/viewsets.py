from rest_framework import authentication
from addresses.models import BuyerAddress
from .serializers import BuyerAddressSerializer
from rest_framework import viewsets


class BuyerAddressViewSet(viewsets.ModelViewSet):
    serializer_class = BuyerAddressSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = BuyerAddress.objects.all()
