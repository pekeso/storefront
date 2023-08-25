from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) # ForeignKey means that each product is associated with a single collection, and each collection can be associated with many products
    promotions = models.ManyToManyField(Promotion) # ManyToManyField means that each product can be associated with many promotions, and each promotion can be associated with many products

class Customer(models.Model):
    BRONZE = 'B'
    SILVER = 'S'
    GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) # unique=True means that no two customers can have the same email address
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True) # null=True means that the birth_date field can be empty
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=BRONZE)

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT) # ForeignKey means that each order is associated with a single customer, and each customer can be associated with many orders

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT) # ForeignKey means that each order item is associated with a single order, and each order can be associated with many order items
    product = models.ForeignKey(Product, on_delete=models.PROTECT) # ForeignKey means that each order item is associated with a single product, and each product can be associated with many order items
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) # OneToOneField means that each customer can have only one address, and each address can belong to only one customer

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) # ForeignKey means that each cart item is associated with a single cart, and each cart can be associated with many cart items
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # ForeignKey means that each cart item is associated with a single product, and each product can be associated with many cart items
    quantity = models.PositiveSmallIntegerField()
    

