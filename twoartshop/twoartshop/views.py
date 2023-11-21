from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def pcs(request):
    return render(request, 'new_pcs.html')


def consoles(request):
    return render(request, 'new_consoles.html')


def login(request):
    pass


def register(request):
    pass


def logout(request):
    pass
