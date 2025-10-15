
from django.urls import path
from Shoe.views import home, Add_Product
urlpatterns = [
    path('', home),
    path('add_product/', Add_Product),
]
