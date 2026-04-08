from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source="menu_item.name", read_only=True)
    class Meta:
        model = OrderItem
        fields = ["id", "menu_item", "menu_item_name", "quantity", "price"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "customer_name", "email", "phone", "total_amount", "order_status", "payment_status", "items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)

        total = 0
        for item_data in items_data:
            menu_item = item_data["menu_item"]
            quantity = item_data["quantity"]
            price = menu_item.price * quantity
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity, price=price)
            total += price

        order.total_amount = total
        order.save()
        return order