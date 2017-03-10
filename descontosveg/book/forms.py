from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome', 'id':'name', 'data-validation-required-message':'Please enter your name.'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail', 'id':'email', 'data-validation-required-message':'Please enter your email adress.'}))
    content = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Content of email', 'id':'content', 'data-validation-required-message':'Please enter a content.'})
    )



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password')    


    first_name = forms.CharField(label=_(u'Primeiro nome'),required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primeiro nome', 'id':'name', 'data-validation-required-message':'Please enter your name.'}))
    last_name = forms.CharField(label=_(u'Ultimo nome'),required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primeiro nome', 'id':'name2', 'data-validation-required-message':'Por favor, digite seu ultimo nome.'}))
    username = forms.CharField(label=_(u'CPF'),required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome', 'id':'name','data-validation-required-message':'Please enter your name.'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail', 'id':'email', 'data-validation-required-message':'Please enter your email adress.'}))
    password = forms.CharField(
        required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Crie uma senha', 'id':'content', 'data-validation-required-message':'Please enter a content.'})
    )