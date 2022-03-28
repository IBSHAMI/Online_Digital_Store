from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# create user library to hold products purchased by user
class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library')
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username


