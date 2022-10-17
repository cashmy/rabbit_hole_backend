from rest_framework import serializers
from .models import Image   

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'file_name', 'url', 'mime_type', 'width', 'height', 'created_at', 'updated_at']
        # fields = "__all__" 