# services.py

import os
import requests

from .models import ProductOnSale

class ProductOnSaleService:
    def __init__(self):
        self.endpoint = f"{os.getenv('STORE_ENGINE_ORCHESTRATOR_PROTOCOL')}://{os.getenv('STORE_ENGINE_ORCHESTRATOR_IP')}:{os.getenv('STORE_ENGINE_ORCHESTRATOR_PORT')}/product"
        self.headers = {"Content-Type": "application/json"}

    def get_product_on_sales(self):
        return ProductOnSale.objects.all()

    def get_product_on_sale_by_id(self, id):
        try:
            return ProductOnSale.objects.get(id_product_on_sale=id)
        except ProductOnSale.DoesNotExist:
            raise ValueError("Product not found")

    def post_product_on_sale(self, product_on_sale_data):
        response = requests.post(self.endpoint, json=product_on_sale_data, headers=self.headers)
        
        if response.status_code != 201:
            raise RuntimeError("Failed to create product on sale")
        else:
            return {"message": "Product creation request sent successfully"}

    def put_product_on_sale(self, id, updated_product_on_sale_data):
        response = requests.put(f"{self.endpoint}/{id}", json=updated_product_on_sale_data, headers=self.headers)

        if response.status_code != 200:
            raise RuntimeError("Failed to update product on sale")
        else:
            return {"message": "Product update request sent successfully"}

    def delete_product_on_sale(self, id):
        response = requests.delete(f"{self.endpoint}/{id}", headers=self.headers)
        
        if response.status_code != 200:
            raise RuntimeError("Failed to delete product on sale")
        else:
            return {"message": "Product delete request sent successfully"}
