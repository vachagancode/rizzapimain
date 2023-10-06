from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RizzSerializer
from .models import Rizz
from .forms import RizzCreationForm
from django.shortcuts import render, redirect

@api_view(['GET'])
def getData(request):
    rizzes = Rizz.objects.all()
    serializer = RizzSerializer(rizzes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = RizzSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def add_rizz(request):
    if request.method != "POST":
        form = RizzCreationForm()
    else:
        form = RizzCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rizz:add')
    context = {
        'form': form
    }
    return render(request, 'add_rizz.html', context)