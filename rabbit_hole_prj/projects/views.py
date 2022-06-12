from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
# from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
def projects_list(request):
    if request.method == "GET":
        print('User(Owner) ', f"{request.user.id} {request.user.email} {request.user.username}")
        projects= Project.objects.filter(user=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print(">>>>> Incoming data: ", f"{request.data}") # Log the data for debugging
        # projects = request.data
        # projects["user_id"] = request.user.id
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            print ("<<< Serializer data: ", f"{serializer.validated_data}")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    print(request.data)
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])    
def projects_admin_list(request):
    if request.method == "GET":
        projects= Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)