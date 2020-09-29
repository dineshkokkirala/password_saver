from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Passwords
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        passwords = Passwords.objects.filter(user_id=request.user.id)
        context = {
            'passwords': passwords
        }
        # print(request.user.email)
        return render(request, 'home/index.html', context)
    else:
        return redirect('login')


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


def hide(request):
    if request.method == 'POST':
        username = request.POST['username']
        websitename = request.POST['websitename']
        websiteurl = request.POST['websiteurl']
        password = request.POST['password']
        email = request.POST['email']
        id_ = request.POST['id']

        context = {
            'username': username,
            'websitename': websitename,
            'websiteurl': websiteurl,
            'password': password,
            'email': email,
            'id': id_
        }
    return render(request, 'home/hide.html', context)


def delete(request, id):
    if request.method == 'POST':
        Passwords.objects.get(id=id).delete()
        return redirect('index')

    return render(request, 'home/hide.html')


def update(request, id, val):
    # print(val)
    user_passwords = Passwords.objects.get(id=id)
    if request.method == 'POST':
       # print(val, user_passwords.websitename)
        if val != user_passwords.websitename:
            username = request.POST['username1']
            websitename = request.POST['websitename']
            websiteurl = request.POST['websiteurl']
            password = request.POST['password']
            email = request.POST['email']
            user_passwords.username = username
            user_passwords.websitename = websitename
            user_passwords.websiteurl = websiteurl
            user_passwords.password = password
            user_passwords.email = email
            user_passwords.save()
            return redirect('index')
        else:
            context = {
                'username': user_passwords.username,
                'websitename': user_passwords.websitename,
                'websiteurl': user_passwords.websiteurl,
                'password': user_passwords.password,
                'email': user_passwords.email,
            }
            return render(request, 'home/update.html', context)

    return render(request, 'home/update.html')
