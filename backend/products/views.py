from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

# PRODUCT LIST CREATE API VIEW
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        brand = serializer.validated_data.get('brand')
        model = serializer.validated_data.get('model') or None
        if model is None:
            model = brand
        serializer.save(model=model)
        
product_list_create_view = ProductListCreateAPIView.as_view()


# PRODUCT DETAIL API VIEW
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
     
product_detail_view = ProductDetailAPIView.as_view()


# Not gonna use this method
# PRODUCT LIST API VIEW
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_list_view = ProductListAPIView.as_view()



@api_view(["GET", "POST"])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method 
    
    if method == "GET":
        if pk is not None:
            #detail view
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise Http404
        #list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        #create an Item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            brand = serializer.validated_data.get('brand')
            model = serializer.validated_data.get('model') or None
            if model is None:
                model = brand
                serializer.save(model=model)
            return Response(serializer.data)
        return Response({"invalid": "not good data"} , status=400)