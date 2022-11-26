from urllib.request import Request
from django.shortcuts import render

# Create your views here.
def education(request):
    contaxt={'education':'active'}
    return render(request, 'edu/skill.html',contaxt)
    