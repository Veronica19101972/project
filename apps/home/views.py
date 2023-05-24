from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, "home/index.html",)

def crear_usuario(request):
        
    form = forms.UsuarioForm()
    context = {"form": form}
    return render(request, "home/crear_usuario.html", context)
    

