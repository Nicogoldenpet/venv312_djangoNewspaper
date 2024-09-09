from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
class SignUpView(CreateView): #Vista signup
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') #Una vez se registre, lo redirigida a login para que ingrese con la cuenta creada.
    template_name = "registration/signup.html"
    
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login después de cerrar sesión