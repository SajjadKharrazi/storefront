from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']

    # products_count = serializers.IntegerField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']

    collection = CollectionSerializer(read_only=True)
    price_with_tax = serializers.SerializerMethodField('calculate_tax_rate')

    def calculate_tax_rate(self, obj: Product):
        return obj.unit_price * Decimal(1.1)
