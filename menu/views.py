from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@gmail.com",
            password="admin123"
        )
        return HttpResponse("Admin created")

    return HttpResponse("Admin already exists")

def home(request):
    return HttpResponse("Foodco Backend is running successfully 🚀")

class MenuListView(generics.ListAPIView):

    queryset = MenuItem.objects.filter(available=True)

    serializer_class = MenuItemSerializer