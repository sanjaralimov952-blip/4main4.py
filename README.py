# 4main4.py
from rest_framework import serializers
from .models import Category, Product, Review


# CATEGORY SERIALIZER
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

    # name бош болбош керек
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Category name must be at least 3 characters")
        return value


# PRODUCT SERIALIZER
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

    # title validation
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters")
        return value

    # price validation
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value

    # description validation
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters")
        return value


# REVIEW SERIALIZER
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

    # text validation
    def validate_text(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Review text must be at least 5 characters")
        return value

    # stars validation (1-5)
    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Stars must be between 1 and 5")
        return value
