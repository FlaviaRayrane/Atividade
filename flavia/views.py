from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')
def cadastro(request):
    return render(request,'base_lista.html')
def form(request):
    return  render(request,'base_form.html')
def login(request):
    return render(request,'login.html')