from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def SignUp(request):
    if request.method == "POST":  
        print(request.POST)
        name  = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("Password")
        em = User.objects.filter(email=email).exists()
        if len(password) > 6 and em == False:
            print(name,email,password)
            user = User.objects.create_user(name, email, password)
            user.save()
            return redirect( "signin")
    
    return render(request, "reg.html")

def SignIn(request):
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            print("Log in Successful")
            return redirect("/")
    return render(request, "log.html")