from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Senetence
from .serializers import SentenceSerializer
from .forms import AddFlirtForm
@api_view(['GET'])
def getData(request):
    sentences = Senetence.objects.all()
    serializer = SentenceSerializer(sentences, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = SentenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def add_flirt(request):
    if request.method != "POST":
        form = AddFlirtForm()
    else:
        form = AddFlirtForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('flirt:add_flirt')
    context = {
        'form': form
    }
    return render(request, 'add_flirt.html', context)