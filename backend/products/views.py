from rest_framework import authentication, generics , mixins , permissions
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
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
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
    # lookup_field = 'pk' 
     
product_detail_view = ProductDetailAPIView.as_view()


# PRODUCT UPDATE API VIEW
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.model:
            instance.model = instance.brand  
     
product_update_view = ProductUpdateAPIView.as_view()


# PRODUCT DELETE API VIEW
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
               
product_delete_view = ProductDeleteAPIView.as_view()


# PRODUCT LIST API VIEW
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_list_view = ProductListAPIView.as_view()

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args,**kwargs):
        print(args,kwargs)
        return self.list(request, *args,**kwargs)

product_mixin_view = ProductMixinView.as_view()

# PRODUCT ALTER API VIEW
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
    
    


# MIXINS
class ProductsView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args,**kwargs)
        return self.list(request, *args,**kwargs)

product_mixin_view = ProductsView.as_view()


class ProductListView(
    mixins.ListModelMixin,
    generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    
    def get(self, request, *args,**kwargs):
        # print(args,kwargs)
        return self.list(request, *args,**kwargs)

product_list_mixin = ProductListView.as_view()


class ProductCreateView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    
    def get(self, request, *args,**kwargs):
        # print(args,kwargs)
        return self.list(request, *args,**kwargs)
    
    def post(self, request, *args,**kwargs):
        # print(args,kwargs)
        return self.create(request, *args,**kwargs)

product_create_mixin = ProductCreateView.as_view()


class ProductRetrieveView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args,**kwargs):
        print(args,kwargs)
        return self.retrieve(request, *args,**kwargs)

product_retrieve_mixin = ProductRetrieveView.as_view()


class ProductUpdateView(
    mixins.UpdateModelMixin,
    generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def patch(self, request, *args,**kwargs):
        print(args,kwargs)
        return self.partial_update(request, *args,**kwargs)
    
    def update(self, request, *args,**kwargs):
        print(args,kwargs)
        return self.update(request, *args,**kwargs)

product_update_mixin = ProductUpdateView.as_view()


class ProductDestroyView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def delete(self, request, *args,**kwargs):
        print(args,kwargs)
        return self.destroy(request, *args,**kwargs)

product_destroy_mixin = ProductDestroyView.as_view()