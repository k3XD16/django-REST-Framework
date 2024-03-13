from django.urls import path

from . import views

# api/products/
urlpatterns = [
    path('',views.product_mixin_view),
    path('list/',views.product_list_mixin),
    path('<int:pk>/',views.product_retrieve_mixin),
    path('<int:pk>/update/',views.product_update_mixin),
    path('<int:pk>/delete/',views.product_destroy_mixin),
    
]
