from django.contrib import admin
from .models import Item


# admin.site.register(Item)
# # Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'short_desc', 'is_publish']
    list_display_links = ['name']
    search_fields= ['name']
    def short_desc(self, item):
        return item.desc[:20]
