from django.urls import path
from .views import OrderCreateView
from .views import InitializePaymentView, VerifyPaymentView

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("pay/<int:order_id>/", InitializePaymentView.as_view()),
    path("verify/<str:reference>/", VerifyPaymentView.as_view()),
]