from django import forms
from Shoe.models import Shoe, Catagory

class Add_Shoe_Form(forms.ModelForm):
    # Category dropdown with Tailwind styling
    Catagory = forms.ModelChoiceField(  # Use the correct field name
        queryset=Catagory.objects.all(),
        empty_label="Select a Category",
        widget=forms.Select(attrs={
            'class': 'block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
        })
    )

    class Meta:
        model = Shoe
        fields = ['name', 'description', 'price', 'image', 'Catagory']  # Use 'Catagory' here