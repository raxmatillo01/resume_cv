from django.contrib import admin

from .models import ContactMessageModel

@admin.register(ContactMessageModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
