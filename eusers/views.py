from rest_framework.response import Response
from rest_framework.decorators import api_view
from .seralizers import UserSerializer
from .models import User
from django.shortcuts import render, redirect

@api_view(['GET'])
def getData(request):
    usernames = User.objects.all()
    serializer = UserSerializer(usernames, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

