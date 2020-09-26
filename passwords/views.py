from django.shortcuts import render

# Create your views here.


def getall(request):
    return render(request, 'passwords/create.html')
