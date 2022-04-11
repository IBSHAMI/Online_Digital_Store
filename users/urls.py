from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from products.views import LandingPageView
from django.conf.urls.static import static
from .views import (
    UserDashboard,
)


app_name = 'users'


urlpatterns = [
    path('', UserDashboard.as_view(), name='user_dashboard'),
]