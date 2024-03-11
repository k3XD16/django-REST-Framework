from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'brand',
            'model',
            'price',
            'discount',
            'sale_price',
            'availability'
        ]

    def get_discount(self,obj):
        print(obj.id)
        print(obj.sale_price)
        return obj.get_discount()