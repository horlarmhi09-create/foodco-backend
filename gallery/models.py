from django.db import models


class Gallery(models.Model):

    CATEGORY_CHOICES = [
        ("food", "Food"),
        ("restaurant", "Restaurant"),
        ("staff", "Staff"),
        ("events", "Events"),
    ]

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to="gallery/")

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title