import requests
from django.conf import settings

PAYSTACK_INITIALIZE_URL = "https://api.paystack.co/transaction/initialize"
PAYSTACK_VERIFY_URL = "https://api.paystack.co/transaction/verify/"


def initialize_payment(email, amount, reference):
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "email": email,
        "amount": int(amount * 100),  # Paystack uses kobo
        "reference": reference,
    }

    response = requests.post(PAYSTACK_INITIALIZE_URL, json=data, headers=headers)
    return response.json()


def verify_payment(reference):
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
    }

    response = requests.get(PAYSTACK_VERIFY_URL + reference, headers=headers)
    return response.json()