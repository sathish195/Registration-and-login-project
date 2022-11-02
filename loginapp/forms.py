from django import forms
from .models import Reg

class RegForm(forms.ModelForm):
    class Meta:
        model=Reg
        fields=['User_Name','First_Name','Last_Name','Email_Id','Phone_Number','password','Con_Password']
        widget={'password': forms.PasswordInput(),
        'Con_Password': forms.PasswordInput()}

class LoginForm(forms.Form):
    User_Name=forms.CharField(max_length=20)
    Password=forms.CharField(widget=forms.PasswordInput())