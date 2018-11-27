#from django.http import HttpResponse
from django.shortcuts import  render

def home(request):
    #return HttpResponse("<h1>Bonjour tout le monde</h1>")
    return render(request, 'pages/home.html')

def account(request):
    #return HttpResponse("<h1>Bonjour tout le monde</h1>")
    return render(request, 'pages/account.html')    

def contact(request):
    #return HttpResponse("<h1>Bonjour tout le monde</h1>")
    return render(request, 'pages/contact.html')    