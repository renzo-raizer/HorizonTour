from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Endereco
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget



class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=100, required=True)
    autenticacao = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'autenticacao')


class UpdateFormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        
class UpdateFormEndereco(forms.ModelForm):
    CEP = forms.CharField(max_length=9)
    endereco= forms.CharField(max_length=100)
    numero= forms.CharField(max_length=8)
    complemento= forms.CharField(max_length=30) 
    bairro = forms.CharField(max_length=50)
    cidade = forms.CharField(max_length=40)
    estado = forms.CharField(max_length=30)
    class Meta:
        model = Endereco
        fields = ['CEP','endereco','numero','complemento','bairro','cidade','estado']
