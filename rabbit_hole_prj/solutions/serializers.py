from rest_framework import serializers
from .models import Solution

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['id', 'type', 'description', 'created_at', 'updated_at']