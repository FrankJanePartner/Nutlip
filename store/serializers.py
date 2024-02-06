from rest_framework import serializers

from .models import Category, Property, PropertyImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ["image", "alt_text"]


class PropertySerializer(serializers.ModelSerializer):
    Property_image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = ["id", "category", "title", "description", "slug", "regular_price", "Property_image"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
