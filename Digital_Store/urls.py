from django.contrib import admin
from django.urls import path, include
from products.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('accounts/', include('allauth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
