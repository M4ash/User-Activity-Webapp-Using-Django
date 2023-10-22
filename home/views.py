#I have imported redirect library for login, logout functionalities
from django.shortcuts import render, redirect
#added manually
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        usern = request.POST.get('username')
        passw = request.POST.get('password')

        # check if the user has entered correct info
        user = authenticate(username=usern, password=passw)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')


def signupUser(request):
    if request.method == "POST":
        frstName = request.POST.get('firstname')
        lstName = request.POST.get('lastname')
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        emailid = request.POST.get('email')

        #Add user...
        user = User.objects.create_user(usern, emailid, passw)
        user.last_name = lstName
        user.first_name = frstName
        user.save()

        messages.success(request, "You have been Signed Up Successfully!")

    return render(request, 'signup.html')