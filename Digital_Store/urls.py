from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from products.views import LandingPageView

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls', namespace='products')),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
