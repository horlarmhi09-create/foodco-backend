from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogSerializer


class BlogListView(generics.ListAPIView):

    queryset = BlogPost.objects.filter(published=True).order_by("-created_at")

    serializer_class = BlogSerializer


class BlogDetailView(generics.RetrieveAPIView):

    queryset = BlogPost.objects.filter(published=True)

    serializer_class = BlogSerializer

    lookup_field = "slug"