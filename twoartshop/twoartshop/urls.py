from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('pcs/', views.pcs, name="pcs"),
    path('consoles/', views.consoles, name="consoles"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register")
]
