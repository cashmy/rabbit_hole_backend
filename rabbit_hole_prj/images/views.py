from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def images_list(request):
    if request.method == "GET":
        images= Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print(request.data) # Log the data for debugging
        serializer = ImageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    print(request.data)
    if request.method == 'GET':
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ImageSerializer(image, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)