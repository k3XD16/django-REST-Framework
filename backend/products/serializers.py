from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'brand',
            'model',
            'price',
            'discount',
            'sale_price',
            'availability'
        ]

    def get_discount(self,obj):
        if not hasattr(obj,'id'):
            return None    
        if not isinstance(obj, Product):
            return None    
        return obj.get_discount()