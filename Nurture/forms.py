from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registration_form(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"username"}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"first_name"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"last_name"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password1"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password2"}))

class login_form(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
    
class order_form(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"address","rows":2}))  