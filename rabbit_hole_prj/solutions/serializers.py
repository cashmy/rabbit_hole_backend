from rest_framework import serializers
from .models import Solution

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['id', 'rabbit_hole', 'rabbit_hole_id', 'type', 'description', 'created_at', 'updated_at']
        depth = 2
        
    rabbit_hole_id = serializers.IntegerField(write_only=True)