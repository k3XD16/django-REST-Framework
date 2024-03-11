from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    
    # if request.method == ['POST']:
    #     return Response({'detail': 'Method "GET" not allowed.'}, status=405)
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance,fields=['id', 'brand', 'model'])
        data = ProductSerializer(instance).data
    return Response(data)
        
