from rest_framework import serializers
from .models import *
class Order_ser (serializers.ModelSerializer):
    class Meta ():
        model= Order
        fields = '__all__'
class Order_Client_ser (serializers.ModelSerializer):
    class Meta ():
        model= Order_Client
        fields = '__all__'
class Basket_ser(serializers.ModelSerializer):
    class Meta ():
        model= Basket
        fields = '__all__'
class Product_ser(serializers.ModelSerializer):
    class Meta ():
        model= Product
        fields = '__all__'
class Product_Backet_ser(serializers.ModelSerializer):
    class Meta ():
        model= Product_Backet
        fields = '__all__'
class Product_category_ser(serializers.ModelSerializer):
    class Meta ():
        model= Product_category
        fields = '__all__'
class Stock_ser(serializers.ModelSerializer):
    class Meta ():
        model= Stock
        fields = '__all__'
class Managere_ser(serializers.ModelSerializer):
    class Meta ():
        model= Managere
        fields = '__all__'
class Provider_ser(serializers.ModelSerializer):
    class Meta ():
        model= Provider
        fields = '__all__'
class Product_ord_provid_ser(serializers.ModelSerializer):
    class Meta ():
        model= Product_order_provider
        fields = '__all__'
class Bill_provider_ser(serializers.ModelSerializer):
    class Meta ():
        model= Bill_provider
        fields = '__all__'
class Order_provider(serializers.ModelSerializer):
    class Meta ():
        model= Order_provider
        fields = '__all__'
class Client_ser (serializers.ModelSerializer):
    class Meta ():
        model= Client
        fields = '__all__'