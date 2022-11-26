from django.shortcuts import render
# from .models import mymessage
# from django.views import View
# from django.contrib import messages
# from flask import request

# Create your views here.
def home(request):
    contaxt={'home':'active'}
    return render(request, 'core/home.html', contaxt)

def contact(request):
    contacm={'contact':'contact'}
    return render(request, 'core/contact.html', contacm)
