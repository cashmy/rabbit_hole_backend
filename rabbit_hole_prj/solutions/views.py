from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Solution
from .serializers import SolutionSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def solutions_all_list(request):
    if request.method == "GET":
        solutions= Solution.objects.all()
        serializer = SolutionSerializer(solutions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def solution_detail(request, pk):
    solution = get_object_or_404(Solution, pk=pk)
    print(request.data)
    if request.method == 'GET':
        serializer = SolutionSerializer(solution)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SolutionSerializer(solution, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        solution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def solutions_list(request, project_id):
    if request.method == "GET":
        solutions= Solution.objects.all()
        serializer = SolutionSerializer(solutions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print(request.data) # Log the data for debugging
        serializer = SolutionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)