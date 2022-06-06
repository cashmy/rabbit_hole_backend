from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Rabbit_Hole
from .serializers import Rabbit_HoleSerializer

# Create your views here.
@api_view(['GET'])
def rabbit_holes_all_list(request):
    if request.method == "GET":
        rabbit_holes= Rabbit_Hole.objects.all()
        serializer = Rabbit_HoleSerializer(rabbit_holes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def rabbit_hole_detail(request, pk):
    rabbit_hole = get_object_or_404(Rabbit_Hole, pk=pk)
    print(request.data)
    if request.method == 'GET':
        serializer = Rabbit_HoleSerializer(rabbit_hole)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = Rabbit_HoleSerializer(rabbit_hole, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        rabbit_hole.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def rabbit_holes_list(request, project_id):
    if request.method == "GET":
        rabbit_holes= Rabbit_Hole.objects.all()
        serializer = Rabbit_HoleSerializer(rabbit_holes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print(request.data) # Log the data for debugging
        serializer = Rabbit_HoleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)