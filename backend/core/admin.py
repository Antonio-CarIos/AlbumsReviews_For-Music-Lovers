from django.contrib import admin
from .models import Profile


class PerfilAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "description","date_joined", "profile_picture")
    search_fields = ("username", "email")


admin.site.register(Profile, PerfilAdmin)
