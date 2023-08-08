from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from datetime import datetime
# Create your models here.











class Product(models.Model):
    product_name = models.CharField(max_length=50, default="")
    product_desc = models.CharField(max_length=300, default="")
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to="images", default="")
    product_file = models.FileField(upload_to="files", default="", blank=True, null=True)
    product_date = models.DateTimeField( blank=True, null=True, default=datetime.now())
    # product_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    product_payment_id = models.CharField(max_length=100, default="", blank=True, null=True)
    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['-product_date']




class CustomUserModel(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=10, default="")
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, default="")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    products_purchased = models.ManyToManyField(Product, blank=True)
   

    # Add or change a related_name argument to the definition for 'auth.User.groups' or 'home.CustomUserModel.groups'.

