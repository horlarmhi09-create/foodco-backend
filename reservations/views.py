from django.shortcuts import render
from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer


class ReservationCreateView(generics.CreateAPIView):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer