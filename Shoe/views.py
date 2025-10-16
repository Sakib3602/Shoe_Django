from django.shortcuts import render
from Shoe.form import Add_Shoe_Form
from Shoe.models import Shoe
# Create your views here.
def home(request):
    x = Shoe.objects.all()
    
    return render(request, 'home.html', {"x" : x})

def Add_Product(request):
    form = Add_Shoe_Form()
    if request.method == "POST":
        form = Add_Shoe_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    
    print("ssc")
    return render(request, 'Product_Add/Add_Product.html', {'form' : form})