# models.py

from django.db import models

class Catalog(models.Model):
    id_product_catalog = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'dim_product_catalog'

class Enterprise(models.Model):
    id_enterprise = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'dim_enterprise'

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, db_column='id_enterprise')

    class Meta:
        db_table = 'dim_product'

class ProductOnSale(models.Model):
    id_product_on_sale = models.AutoField(primary_key=True, db_column='id_product_on_sale')
    title = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='id_product')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, db_column='id_product_catalog')
    price = models.FloatField()
    sale_start_datetime = models.DateTimeField(db_column='sale_start_datetime')
    sale_end_datetime = models.DateTimeField(db_column='sale_end_datetime')

    class Meta:
        db_table = 'fact_product_on_sale'
