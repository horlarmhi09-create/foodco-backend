from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):

    list_display = ("title", "published", "created_at")

    list_filter = ("published",)

    search_fields = ("title",)

    prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogPost, BlogAdmin)