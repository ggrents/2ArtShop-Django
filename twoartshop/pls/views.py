from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def index(request):
    return render(request, 'index.html', {"user": request.user})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def pcs(request):
    return render(request, 'new_pcs.html', {"user":request.user})


def consoles(request):
    return render(request, 'new_consoles.html', {"user":request.user})


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             usname = request.POST['username']
#             passw = request.POST['password']
#             user = authenticate(request, username=usname, password=passw)
#             if user is not None:
#                 login(request, user)
#                 return redirect('main-page')
#             else:
#                 return redirect('signin')
#     else:
#         form = AuthenticationForm()
#
#     return render(request, 'login.html', {'form': form})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def logout(request):
    pass
