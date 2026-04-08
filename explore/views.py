from django.shortcuts import render
from rest_framework import generics
from .models import Explore
from .serializers import ExploreSerializer


class ExploreListView(generics.ListAPIView):

    queryset = Explore.objects.filter(active=True).order_by("-created_at")

    serializer_class = ExploreSerializer