from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                    user.save()
                    messages.success(
                        request, 'You are now registerd and can login')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'users/register.html')


def login(request):
    return render(request, 'users/login.html')
