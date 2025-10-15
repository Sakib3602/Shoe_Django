from django import forms
from Shoe.models import Shoe, Catagory
class Add_Shoe_Form(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['name', 'description', 'price', 'image', 'Catagory']     
        
        