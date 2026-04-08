from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .paystack import initialize_payment, verify_payment

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class InitializePaymentView(APIView):

    def post(self, request, order_id):

        order = get_object_or_404(Order, id=order_id)

        response = initialize_payment(
            email=order.email,
            amount=order.total_amount,
            reference=str(order.payment_reference)
        )

        return Response(response)


class VerifyPaymentView(APIView):

    def get(self, request, reference):

        response = verify_payment(reference)

        if response["data"]["status"] == "success":

            order = Order.objects.get(payment_reference=reference)
            order.payment_status = True
            order.order_status = "paid"
            order.save()

        return Response(response)