# views.py
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, UserListSerializer, UserDetailSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import ProductFilter, UserProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['price']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserDetailSerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        user = self.get_object()
        products = Product.objects.filter(created_by=user)
        filterset = UserProductFilter(request.GET, queryset=products)
        if filterset.is_valid():
            products = filterset.qs
        else:
            return Response({'error': 'Invalid filter parameters'}, status=400)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
