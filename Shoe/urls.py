
from django.urls import path
from Shoe.views import home
urlpatterns = [
    path('', home),
]
