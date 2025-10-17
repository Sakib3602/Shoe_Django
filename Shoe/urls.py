
from django.urls import path
from Shoe.views import home, Add_Product , Details_Page ,Update, Delete
urlpatterns = [
    path('', home),
    path('add_product/', Add_Product,name="add_product"),
    path("details/<int:id>", Details_Page, name='details'),
    path("update/<int:id>" , Update , name = "update"),
    path("del/<int:id>" ,  Delete, name = "delete"),
]
