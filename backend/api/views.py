from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    
    # if request.method == ['POST']:
    #     return Response({'detail': 'Method "GET" not allowed.'}, status=405)
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data,fields=['id', 'brand', 'model'])
    return Response(data)
        
