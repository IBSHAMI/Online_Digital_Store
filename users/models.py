from django.db import models
from products.models import Products

# import the User model created by allauth
from django.conf import settings
User = settings.AUTH_USER_MODEL


# create user library to hold products purchased by user
class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library')
    product = models.ManyToManyField(Products, blank=True)

    # edit the plural name of the model
    class Meta:
        verbose_name_plural = 'User Libraries'

    def __str__(self):
        return self.user.username + " Library"
