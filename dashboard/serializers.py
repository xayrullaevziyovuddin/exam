# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, source='product_set', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'products']
