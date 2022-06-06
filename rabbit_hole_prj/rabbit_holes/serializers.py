from rest_framework import serializers
from .models import Rabbit_Hole

class Rabbit_HoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rabbit_Hole
        fields = ['id', 'project', 'project_id', 'log_type', 'name', 'description',
                  'rating', 'solution', 'archived', 'created_at', 'updated_at']
        depth = 1
        
    project_id = serializers.IntegerField(write_only=True)