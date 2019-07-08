from django.http import QueryDict
from url_filter.filtersets import ModelFilterSet
from .models import *

class ProductFilterSet(ModelFilterSet):
    class Meta(object):
        model = Product

query = QueryDict('category__in=dog,cat,fish')
fs = ProductFilterSet(data=query, queryset=Product.objects.all())
filtered_users = fs.filter()
