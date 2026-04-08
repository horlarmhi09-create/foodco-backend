from django.contrib import admin
from .models import ContactMessage


class ContactAdmin(admin.ModelAdmin):

    list_display = ("name", "email", "created_at")

    search_fields = ("name", "email")


admin.site.register(ContactMessage, ContactAdmin)
