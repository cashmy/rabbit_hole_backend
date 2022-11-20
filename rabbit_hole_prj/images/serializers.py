from rest_framework import serializers
from .models import Image   

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'file_name', 'alt_text', 'mime_type', 'file_size', 'user', 'user_id', 'created_at', 'updated_at']
        depth = 1
        
        user_id = serializers.IntegerField(write_only=True)