from django.shortcuts import render
from rest_framework import generics

from . import models
from .models import Category, Property
from .serializers import CategorySerializer, PropertySerializer


class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class Property(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class CategoryItemView(generics.ListAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        return models.Property.objects.filter(
            category__in=Category.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(level=1)
    serializer_class = CategorySerializer
