from django.shortcuts import render

# Create your views here.
def SignUp(request):
    return render(request, "reg.html")

def SignIn(request):
    return render(request, "log.html")