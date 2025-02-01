from django.contrib import admin
from django.urls import path
from ideas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup', views.signup_page, name='signup_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),

    path('publicpage', views.public_page, name='public_page'),
    path('szkolenia/', views.lista_szkolen, name='lista_szkolen'),
    path('custom-admin/', views.custom_admin_panel, name='custom_admin_panel'),
    path('custom-admin/edytuj/<int:szkolenie_id>/', views.edytuj_szkolenie, name='edytuj_szkolenie'),
    path('custom-admin/usun/<int:szkolenie_id>/', views.usun_szkolenie, name='usun_szkolenie'),
    path('dodaj-szkolenie/', views.dodaj_szkolenie, name='dodaj_szkolenie'),
    path('zapisz-na-szkolenie/<int:szkolenie_id>/', views.zapisz_na_szkolenie, name='zapisz_na_szkolenie'),
    path('lista-zapisow/<int:szkolenie_id>/', views.lista_zapisow, name='lista_zapisow'),
]