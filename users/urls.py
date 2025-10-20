from django.urls import path
from users.views import SignUp ,SignIn,logOut_User

urlpatterns = [
    path("signup/" , SignUp, name="signup"),
    path("signin/" , SignIn, name="signin"),
    path("logout/" , logOut_User, name="logout"),
]