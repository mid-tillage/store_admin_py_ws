from rest_framework import serializers
from .models import ProductOnSale

class ProductOnSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOnSale
        fields = '__all__'
