from rest_framework import serializers
from addresses.models import BuyerAddress


class BuyerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerAddress
        fields = "__all__"
