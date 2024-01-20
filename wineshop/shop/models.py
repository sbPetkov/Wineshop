import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True)
    password = models.CharField(max_length=255)


class Wine(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=1)
    # Add sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.title


class Orders(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]

    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    email = models.EmailField()
    shipping_address = models.TextField()
    order_date = models.DateTimeField(default=datetime.datetime.today)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    items = models.ManyToManyField(Wine)
    quantity = models.PositiveIntegerField(default=1)
    address = models.CharField(max_length=100, default="No Address", blank=True)
    phone = models.CharField(max_length=20, default="No Phone", blank=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

