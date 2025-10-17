from django.urls import path
from users.views import SignUp ,SignIn

urlpatterns = [
    path("signup/" , SignUp, name="signup"),
    path("signin/" , SignIn, name="signin"),
]