from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome', 'id':'name', 'data-validation-required-message':'Please enter your name.'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail', 'id':'email', 'data-validation-required-message':'Please enter your email adress.'}))
    content = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Content of email', 'id':'content', 'data-validation-required-message':'Please enter a content.'})
    )