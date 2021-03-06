from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=250, required=True)
    last_name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=250, help_text='eg. youremail@hotmail.com')
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2' )
    
class ContactUsForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    name = forms.CharField(max_length=50, required=True)
    from_email = forms.EmailField(max_length=50, required=True)
    message = forms.CharField(
        max_length=100,
        widget=forms.Textarea(),
        help_text ='Write here your message'
        )

    
