# filters.py
import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    category_name = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    price = django_filters.NumberFilter(field_name='price', lookup_expr='exact')

    class Meta:
        model = Product
        fields = ['category_name', 'price']


class UserProductFilter(ProductFilter):
    created_by = django_filters.NumberFilter(field_name='created_by', lookup_expr='exact')

    class Meta(ProductFilter.Meta):
        fields = ProductFilter.Meta.fields + ['created_by']
