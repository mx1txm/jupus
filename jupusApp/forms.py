
from django import forms
from .models import Client, LegalRequest, DocumentAttachment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LegalRequestForm(forms.ModelForm):
    class Meta:
        model = LegalRequest
        fields = ['case_description', 'case_type', 'status']



class DocumentAttachmentForm(forms.ModelForm):
    class Meta:
        model = DocumentAttachment
        fields = ['document']
