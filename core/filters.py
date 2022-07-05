from django.contrib.auth.models import User
import django_filters
from .models import UserProfile ,Item , OrderItem, Order ,Address ,Payment ,Coupon,Refund

class UserProfileFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = ['user_name',]
    
class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['item_name',]




class OrderItemFilter(django_filters.FilterSet):
    class Meta:
        mode = OrderItem
        fields = ['order_item',]

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['order',]
        
class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['order',]

