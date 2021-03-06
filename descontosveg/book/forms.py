from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome', 'id':'name', 'data-validation-required-message':'Escreva um nome.'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail', 'id':'email', 'data-validation-required-message':'Digite um e-mail.'}))
    telefone = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefone', 'id':'telefone'})
    )
    content = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite sua mensagem', 'id':'content', 'data-validation-required-message':'Por favor coloque uma mensagem.'})
    )



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password')    


    first_name = forms.CharField(label=_(u'Primeiro nome'),required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primeiro nome', 'id':'name', 'data-validation-required-message':'Please enter your name.'}))
    last_name = forms.CharField(label=_(u'Ultimo nome'),required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome', 'id':'name2', 'data-validation-required-message':'Por favor, digite seu ultimo nome.'}))
    username = forms.CharField(label=_(u'CPF'),required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CPF', 'id':'name','data-validation-required-message':'Please enter your name.'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail', 'id':'email', 'data-validation-required-message':'Please enter your email adress.'}))
    password = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Crie uma senha', 'id':'content', 'data-validation-required-message':'Please enter a content.'})
    )