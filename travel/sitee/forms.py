from django import forms
from .models import Profile

class ProfileRegistration(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["Name", "Date_of_birth","Gender","Phone_number"]
        widgets = {
            "Name": forms.TextInput(),
            "Date_of_birth": forms.DateField(),
            "Gender": forms.TextInput(), 
            "Phone_number":forms.IntegerField(),           
        }