from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#ProductForm

class CadastroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email'] 


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
