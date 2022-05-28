import email
from msilib.schema import Class
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class RegisterForm(UserCreationForm): 
    email = forms.EmailField(label='E-mail')

    #salvando cadastro user
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    #verificação se e-mail já existe no db
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário com este e-mail')
        else:
            return email










