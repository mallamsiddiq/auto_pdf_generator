import django_filters
from .models import Document,Transaction
from django_filters import rest_framework as drf_filters
class DocFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields = ['transaction']


