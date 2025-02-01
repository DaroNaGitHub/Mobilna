from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Szkolenia, Zapis
from django.contrib.admin.views.decorators import staff_member_required
from .forms import SzkoleniaForm
from django.shortcuts import get_object_or_404, redirect, render
# from .models import Idea, Vote
# from rest_framework import viewsets 
# from serjalizer import IdeaSerializer, VotSerializer


# class IdeaViewSet(viewsets.ModelViewSet):
#     queryset = Idea.objects.all()
#     serializer_class = IdeaSerializer


# class VoteViewSet(viewsets.ModelViewSet):
#     queryset = Vote.objects.all()
#     serializer_class = VotSerializer
    




def home(request):
    context = {}
    if request.user.is_authenticated:
        context['userStatus'] = 'zalogowany:  ' 
    else:
        context['userStatus'] = 'niezalogowany'
    return render(request, 'ideas/publicpage.html', context)

def signup_page(request):
    context = {}
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            context['error'] = 'Podana nazwa użytkownika już istnieje! Proszę podać inną nazwę użytkownika.'
            return render(request, 'ideas/signup.html', context)
        except User.DoesNotExist:
            if request.POST['first_name'] =='':
                context['error'] = 'Imię jest wymagane!'
                return render(request, 'ideas/signup.html', context)
            
            if request.POST['last_name'] =='':
                context['error'] = 'Nazwisko jest wymagane!'
                return render(request, 'ideas/signup.html', context)
            
            if request.POST['email'] =='':
                context['error'] = 'e-mail jest wymagany!'
                return render(request, 'ideas/signup.html', context)
            
            if request.POST['password1'] !='':
                if request.POST['password1'] != request.POST['password2']:
                    context['error'] = 'Podane hasła nie są takie same! Proszę wprowadzić identyczne hasła.'
                    return render(request, 'ideas/signup.html', context)
                else:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
                    auth.login(request, user)
                    return redirect('home')
            else:
                context['error'] = 'Hasło jest wimagane'
                return render(request, 'ideas/signup.html', context)                
    else:
        return render(request, 'ideas/signup.html', context)

def login_page(request):
    context = {}
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'] ,password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if request.POST.get('redir'):
                return redirect(f"{request.POST.get('redir')}")
            else:
                return redirect('home')
        else:
            context['error'] = 'Podane hasło lub login są błędne! Podaj poprawne dane.'
            if request.POST.get('redir'):
                context['next'] = 'Tylko zalogowani użytkonicy mają dostęp do tej strony! Zaloguj się.'
                context['nextURL'] = request.GET.get('next')
            return render(request, 'ideas/login.html', context)
    else:
        if request.GET.get('next'):
            context['next'] = 'Tylko zalogowani użytkonicy mają dostęp do tej strony! Zaloguj się.'
            context['nextURL'] = request.GET.get('next')
        return render(request, 'ideas/login.html', context)
        
def logout_page(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def public_page(request):
    return render(request, 'ideas/publicpage.html')


@staff_member_required
def custom_admin_panel(request):
    szkolenia = Szkolenia.objects.all() 
    return render(request, 'ideas/custom_admin.html', {'szkolenia': szkolenia})

@staff_member_required
def usun_szkolenie(request, szkolenie_id):
    szkolenie = get_object_or_404(Szkolenia, id=szkolenie_id)
    if request.method == 'POST':
        szkolenie.delete()
        return redirect('custom_admin_panel')
    return render(request, 'ideas/usun_szkolenie.html', {'szkolenie': szkolenie})

@staff_member_required
def dodaj_szkolenie(request):
    if request.method == 'POST':
        form = SzkoleniaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custom_admin_panel')  # Powrót do panelu administracyjnego
    else:
        form = SzkoleniaForm()

    return render(request, 'ideas/dodaj_szkolenie.html', {'form': form})


def lista_szkolen(request):
    szkolenia = Szkolenia.objects.all()  # Pobranie wszystkich ogłoszeń z bazy
    return render(request, 'ideas/lista.html', {'szkolenia': szkolenia})



@staff_member_required
def edytuj_szkolenie(request, szkolenie_id):
    szkolenie = get_object_or_404(Szkolenia, id=szkolenie_id)  # Pobierz szkolenie lub zwróć 404
    if request.method == 'POST':
        form = SzkoleniaForm(request.POST, instance=szkolenie)  # Przypisz dane POST do istniejącego szkolenia
        if form.is_valid():
            form.save()
            return redirect('custom_admin_panel')  # Powrót do panelu administracyjnego
    else:
        form = SzkoleniaForm(instance=szkolenie)  # Wypełnij formularz istniejącymi danymi

    return render(request, 'ideas/edytuj_szkolenie.html', {'form': form})


@login_required
def zapisz_na_szkolenie(request, szkolenie_id):
    szkolenie = get_object_or_404(Szkolenia, id=szkolenie_id)

    # Sprawdzenie, czy użytkownik już zapisany
    if Zapis.objects.filter(user=request.user, szkolenie=szkolenie).exists():
        return render(request, 'ideas/message.html', {
            'message': 'Już jesteś zapisany na to szkolenie.'
        })

    # Sprawdzenie dostępności miejsc
    if szkolenie.available_spots <= 0:
        return render(request, 'ideas/message.html', {
            'message': 'Brak wolnych miejsc na to szkolenie.'
        })

    # Tworzenie zapisu
    zapis = Zapis.objects.create(user=request.user, szkolenie=szkolenie)
    szkolenie.available_spots -= 1
    szkolenie.save()

    return render(request, 'ideas/message.html', {
        'message': 'Zostałeś zapisany na szkolenie!'
    })


@staff_member_required
def lista_zapisow(request, szkolenie_id):
    szkolenie = get_object_or_404(Szkolenia, id=szkolenie_id)
    zapisy = Zapis.objects.filter(szkolenie=szkolenie)

    return render(request, 'ideas/lista_zapisow.html', {
        'szkolenie': szkolenie,
        'zapisy': zapisy,
    })