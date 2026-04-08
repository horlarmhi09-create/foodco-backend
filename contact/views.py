from django.shortcuts import render
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings

from .models import ContactMessage
from .serializers import ContactSerializer


class ContactCreateView(generics.CreateAPIView):

    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):

        message = serializer.save()

        subject = "New Contact Message - FoodCo"

        email_message = f"""
You have received a new contact message.

Name: {message.name}
Email: {message.email}
Phone: {message.phone}

Message:
{message.message}
"""

        send_mail(
            subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            ["giwajamiu00@gmail.com"],
            fail_silently=False,
        )