from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TaskModel
from .serializers import TaskSerializer

@api_view(['GET'])
def get(request):
    tasks = TaskModel.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    ser = TaskSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)