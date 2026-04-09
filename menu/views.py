from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="jamiu",
            email="horlarmhi09@gmail.com",
            password="giwa,.00jamiu"
        )
        return HttpResponse(f"{username} you now have access to the django foodco backend admin dashboard")

    return HttpResponse("You are already a super user")

def home(request):
    return HttpResponse("Foodco Backend is running successfully 🚀")

class MenuListView(generics.ListAPIView):

    queryset = MenuItem.objects.filter(available=True)

    serializer_class = MenuItemSerializer