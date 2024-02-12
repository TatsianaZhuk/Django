from django.contrib import admin
from .models import Mebel

class MebelAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'parse_datetime', 'description']
    list_display_link = ['id', 'parse_datetime']
    search_fields = ['id', 'price', 'parse_datetime', 'description']
    # list_editable = ['price']
    list_filter = ['parse_datetime', 'price']

admin.site.register(Mebel, MebelAdmin)
