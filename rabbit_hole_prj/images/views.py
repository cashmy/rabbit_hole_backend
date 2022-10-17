from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    print(request.data)
    if request.method == 'GET':
        serializer = ImageSerializer(image)
        print("Data", serializer.data)
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
    
@api_view(['GET'])
@permission_classes([AllowAny])
def image_file(request, file):
    print("\n\nRequest: ", request)
    print("file: ", file)
    image = Image.objects.filter(file_name__endswith=file)
    print(len(image))
    print("Media result: ",image)
    if request.method == 'GET':
        serializer = ImageSerializer(image, many=True)
        print("Data", serializer.data)
        
    return Response(serializer.data, status=status.HTTP_200_OK)