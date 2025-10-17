from django.shortcuts import render, redirect
from Shoe.form import Add_Shoe_Form
from Shoe.models import Shoe
# Create your views here.
def home(request):
    x = Shoe.objects.select_related("Catagory").all()
    
    return render(request, 'home.html', {"x" : x})

def Details_Page(request,id):
    x = Shoe.objects.get(id=id)
    
    
    return render(request, 'details_page/details.html',{ "shoe" : x})

def Add_Product(request):
    form = Add_Shoe_Form()
    if request.method == "POST":
        form = Add_Shoe_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('/')
    return render(request, 'Product_Add/Add_Product.html', {'form' : form})

def Update(request,id):
    shoe = Shoe.objects.get(id=id)
    form = Add_Shoe_Form()
    if request.method == "POST":
        form = Add_Shoe_Form(request.POST , request.FILES, instance=shoe)
        if form.is_valid():
            form.save()
            
            return redirect('/')
    return render(request, 'UpdateProduct/Update.html', {'form' : form})


def Delete(request,id):
    shoe = Shoe.objects.get(id=id)
    Shoe.delete(shoe)
    return redirect('/')
    
