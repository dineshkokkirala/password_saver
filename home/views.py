from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Passwords


def index(request):
    return render(request, 'home/index.html')


def create(request):
    if request.method == 'POST':
        websitename = request.POST['websitename']
        websiteurl = request.POST['websiteurl']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        user_id = request.POST['user_id']
        if password == password2:
            if Passwords.objects.filter(websitename=websitename, user_id=user_id, email=email).exists():
                messages.error(request, 'Website already exists')
                return redirect('index')
            else:
                temp = Passwords(websitename=websitename, websiteurl=websiteurl,
                                 username=username, email=email, password=password, user_id_id=user_id)
                temp.save()
                messages.success(request, 'Successfully record added')
                return redirect('index')
        else:
            messages.error(request, 'Passwords must be equal')
            return redirect('index')
    else:
        return render(request, 'home/index.html')
