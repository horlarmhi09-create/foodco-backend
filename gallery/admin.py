from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):

    list_display = ("title", "category", "created_at")

    list_filter = ("category",)

    search_fields = ("title",)


admin.site.register(Gallery, GalleryAdmin)