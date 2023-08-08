from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Product
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model()

admin.site.register(User)

admin.site.site_header = "Image Commerce Admin"
admin.site.site_title = "Image Commerce Admin Portal"
admin.site.index_title = "Welcome to Image Commerce Portal"

admin.site.unregister(Group)


admin.site.register(Product)


