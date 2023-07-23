
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    #suggestions = serializers.SerializerMethodField()
    suggestions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        #exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
        #depth = 1

    def get_suggestions(self, product):
        # Retrieve the related suggestions and serialize them
        suggestions = ProductSerializer(product.suggestions.all(), many=True).data
        return suggestions
"""
from rest_framework import serializers
from .models import Product, Suggestion


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    suggestions = SuggestionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
"""