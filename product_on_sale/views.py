from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product_on_sale.serializers import ProductOnSaleSerializer
from .models import ProductOnSale
from .services import ProductOnSaleService
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

product_on_sale_service = ProductOnSaleService()
# Friendly reminder: If non example, return the receiver's retrieved data  / man in the middle casuistry check
@swagger_auto_schema(method='get', responses={200: ProductOnSaleSerializer(many=True)}, operation_description="Retrieve all products on sale.")
@swagger_auto_schema(method='post', request_body=ProductOnSaleSerializer, responses={201: "Product creation request sent successfully"}, operation_description="Create a new product on sale.")
@api_view(['GET', 'POST'])
def product_on_sale(request):
    """
    Retrieve all or update a product on sale.
    """
    if request.method == 'GET':
        product_on_sales = product_on_sale_service.get_product_on_sales()
        serializer = ProductOnSaleSerializer(product_on_sales, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        product_on_sale = product_on_sale_service.post_product_on_sale(request.data)
        serializer = ProductOnSaleSerializer(product_on_sale)
        return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: ProductOnSaleSerializer()}, operation_description="Retrieve a product on sale by ID.")
@swagger_auto_schema(method='put', request_body=ProductOnSaleSerializer, responses={200: "Product update request sent successfully"}, operation_description="Update a product on sale by ID.")
@swagger_auto_schema(method='delete', responses={200: "Product delete request sent successfully"}, operation_description="Delete a product on sale by ID.")
@api_view(['GET', 'PUT', 'DELETE'])
def product_on_sale_detail(request, id):
    """
    Retrieve, update or delete a product on sale by ID.
    """
    try:
        product_on_sale = product_on_sale_service.get_product_on_sale_by_id(id)
    except ProductOnSale.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProductOnSaleSerializer(product_on_sale)
        return Response(serializer.data)
    elif request.method == 'PUT':
        return Response(product_on_sale_service.put_product_on_sale(id, request.data))
    elif request.method == 'DELETE':
        return Response(product_on_sale_service.delete_product_on_sale(id))
