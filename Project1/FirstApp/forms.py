from django import forms
from .models import Address

class AddressModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'