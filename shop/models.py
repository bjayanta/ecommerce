from itertools import product
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    wholesale_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    retail_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to="media/")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isFavorite = models.BooleanField(default=False)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        return f"Product ID = {self.product.name} ({self.product.id}) | Username = {self.user.username} | Is Favorite = {self.isFavorite}"
    
class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, help_text="In percentage")
    isComplete = models.BooleanField(default=False)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        return f"User = {self.user.username} | Complete = {self.isComplete}"
    
class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "sale_details"

    def __str__(self):
        return f"Sale ID = {self.sale.id} | Product = {self.product.name} ({self.product.id})"

class Order(models.Model):
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    