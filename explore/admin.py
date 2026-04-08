from django.contrib import admin
from .models import Explore


class ExploreAdmin(admin.ModelAdmin):

    list_display = ("title", "active", "created_at")

    list_filter = ("active",)

    search_fields = ("title",)


admin.site.register(Explore, ExploreAdmin)