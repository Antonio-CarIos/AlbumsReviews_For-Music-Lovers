from django.contrib import admin
from .models import List


class ListAdmin(admin.ModelAdmin):
    list_display = ("name_list", "mini_description")
    search_fields = ("name_list",)


admin.site.register(List, ListAdmin)
