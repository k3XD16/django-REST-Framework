from django.urls import path

from . import views

# api/products/
urlpatterns = [
    path('',views.product_list_create_view),
    path('list/',views.product_list_view),
    path('<int:pk>/',views.product_detail_view),
    
]
