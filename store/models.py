from django.db import models
from django.conf import settings
from django.contrib import admin
from django.core.validators import MinValueValidator
from uuid import uuid4

# Create your models here.

# Many-Many rel with Promotion-Product


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


# 1-Many rel with Collection-Product


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True,  related_name='+', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


# Product Model


class Product(models.Model):
    # sku = models.CharField(max_length=10, primary_key=True)  if required
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, validators=[
                                     MinValueValidator(1)])
    inventory = models.IntegerField(validators=[
        MinValueValidator(0)])
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, related_name='products')
    promotions = models.ManyToManyField(Promotion, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

# Customer Model


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'N'
    MEMBERSHIP_SILVER = 'R'
    MEMBERSHIP_GOLD = 'L'
    MEMBERSHIP_CHICES = [
        (MEMBERSHIP_BRONZE, 'Normal'),
        (MEMBERSHIP_SILVER, 'Regular'),
        (MEMBERSHIP_GOLD, 'Loyal'),
    ]

    phone = models.CharField(max_length=255)

    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHICES, default=MEMBERSHIP_BRONZE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}{self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

# Order Model


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),

    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return f'Order {self.id} placed by {self.customer}'

    # class Meta:
    #     ordering = ['customer__last_name', 'customer__first_name', 'placed_at']

    class Meta:
        permissions = [
            ('cancel_order', 'Can cancel order')
        ]
# 1-many rel with Order-Item


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


# 1-Many relationship with Customer & Address


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    Customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)


# Shopping Cart


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


# 1-many rel with CartItem
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'product']]


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
