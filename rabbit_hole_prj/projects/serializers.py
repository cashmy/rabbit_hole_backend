from rest_framework import serializers
from .models import Project    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [ 'id', 'name', 'abbreviation', 'description', 'user', 'user_id', 'text_color', 'theme_color',
                  'image', 'image_id', 'created_at', 'updated_at' ]
        depth = 1
        
    user_id = serializers.IntegerField(write_only=True)
    image_id = serializers.IntegerField(write_only=True)