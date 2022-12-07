from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Rabbit_Hole
from .serializers import Rabbit_HoleSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def rabbit_holes_all_list(request):
    if request.method == "GET":
        rabbit_holes= Rabbit_Hole.objects.all()
        serializer = Rabbit_HoleSerializer(rabbit_holes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([AllowAny])
# http://127.0.0.1:8000/api/rabbit_hole/1/
def rabbit_hole_detail(request, pk):
    rabbit_hole = get_object_or_404(Rabbit_Hole, pk=pk)
    if request.method == 'GET':
        serializer = Rabbit_HoleSerializer(rabbit_hole)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = Rabbit_HoleSerializer(rabbit_hole, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("\n\nSerializer Error(s): ", f"{serializer.errors}")
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        rabbit_hole.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PATCH':
        print("Patch requested")
        serializer = Rabbit_HoleSerializer(rabbit_hole, data= request.data, partial=True)
        if serializer.is_valid():
            print("Patch is valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("\n\nSerializer Error(s): ", f"{serializer.errors}")
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def rabbit_holes_list(request, project_id):
    print("\n\nRequest Data: ", request.data)
    if request.method == "GET":
        rabbit_holes = Rabbit_Hole.objects.filter(project_id=project_id)
        serializer = Rabbit_HoleSerializer(rabbit_holes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print(request.data) # Log the data for debugging
        serializer = Rabbit_HoleSerializer(data = request.data)
        if serializer.is_valid():
            print ("<<< Serializer data: ", f"{serializer.validated_data}")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("\n\nSerializer Error(s): ", f"{serializer.errors}")
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)