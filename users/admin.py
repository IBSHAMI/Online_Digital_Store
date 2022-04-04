from django.contrib import admin
from .models import UserLibrary


# register models in this app to admin
class UserLibraryAdmin(admin.ModelAdmin):
    search_fields = ('user', 'Products')
    list_per_page = 25


admin.site.register(UserLibrary, UserLibraryAdmin)