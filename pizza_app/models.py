from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    # contact_phone = PhoneNumberField(unique=True)
    address = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.id} {self.name} '


CATEGORY_CHOICES =(
    ('snack', "snack"),
    ('pizza', "pizza"),
    ('dessert', "dessert"),
    ('drink', "drink"),
)

MEASUREMENT_CHOICES =(
    ('liters', "liters"),
    ('pieces', "pieces"),
    ('kilograms', "kilograms"),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=150, choices=CATEGORY_CHOICES)
    unit_of_measurement = models.CharField(max_length=150, choices=MEASUREMENT_CHOICES)
    minimum_stock_level = models.IntegerField(default= 50)
    best_before_date = models.FloatField(default= 0.1)
    supplier = models.ManyToManyField(Supplier,related_name="products")
    price = models.FloatField(default= 0.1)

    def __str__(self):
        return f'{self.id} {self.name} {self.price} {self.supplier}'

class Pizzaplace(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    contact_email = models.EmailField()
    # contact_phone = PhoneNumberField(unique=True)

    def __str__(self):
        return f'{self.id} {self.name}'

class Warehouse(models.Model):
    Pizzahouse = models.ForeignKey(Pizzaplace, on_delete=models.CASCADE, related_name="warehouses")

    def __str__(self):
        return f'{self.id} Pizzahouse:{self.Pizzahouse.name}'

class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="warehouse_product")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_warehouse")
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id} {self.product.name} {self.quantity}'
