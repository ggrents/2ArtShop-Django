from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from pls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('pcs/', views.pcs, name="pcs"),
    path('consoles/', views.consoles, name="consoles"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', views.register, name="register")
]
