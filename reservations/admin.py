from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "guests",
        "reservation_date",
        "reservation_time",
        "status",
    )

    list_filter = ("reservation_date", "status")

    search_fields = ("name", "email", "phone")


admin.site.register(Reservation, ReservationAdmin)