from urllib import request
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterForm

class SignUp(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login') #quando se cadastrar vai ser redirecionado para o login
    template_name = 'registration/register.html'

    


    