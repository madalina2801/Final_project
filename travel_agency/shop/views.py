from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


from shop.forms import SignUpForm

def aaa(request):
    return HttpResponse("This is aaa page, returned by aaa view!")

#functional view

# functional view
# def main_page(request):
#     return render(request, template_name="main_page.html", context={"n": range(5)})


def logout_view(request):
    logout(request)
    return redirect('login')

# Class-Based view (CBV)
class MainPage(TemplateView):
    template_name = 'main_page.html'

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')


    
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
