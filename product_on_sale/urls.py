# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('product-on-sale', views.product_on_sale),
    path('product-on-sale/<int:id>', views.product_on_sale_detail)
]
