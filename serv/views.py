from django.shortcuts import render

# Create your views here.
def services(request):
    contaxt={'services':'active'}
    return render(request, 'serv/services.html', contaxt)