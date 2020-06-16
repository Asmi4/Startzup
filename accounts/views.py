from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # The user wants to sign up! wants an account now
        if request.POST['password1'] == request.POST['password2']:

            try:
                user= User()
                x= request.POST['username']
                user = User.objects.get_by_natural_key(username=x)
                user.save()
                return render(request,'accounts/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')

    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html',{'error':'Passwords must match'})
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error': 'username or password is incorrect'})


    else:
        return render(request,'accounts/login.html')

def logout(request):
    #TODO Need to route to homepage
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    return render(request,'accounts/signup.html')