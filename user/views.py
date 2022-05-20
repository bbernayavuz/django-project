from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from user.forms import RegisterForm, LoginForm




# Create your views here.
def users(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {
            'users': users
        })

def user_register_form(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def user_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/user/list')



def user_login(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username= form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/user/list')
            
        else:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

    return render(request, 'login.html', context)
