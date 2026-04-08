from django.shortcuts import render
from rest_framework import generics
from .models import Gallery
from .serializers import GallerySerializer


class GalleryListView(generics.ListAPIView):

    queryset = Gallery.objects.all().order_by("-created_at")
    serializer_class = GallerySerializer