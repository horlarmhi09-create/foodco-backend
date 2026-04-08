from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuListView(generics.ListAPIView):

    queryset = MenuItem.objects.filter(available=True)

    serializer_class = MenuItemSerializer