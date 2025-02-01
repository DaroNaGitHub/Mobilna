from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('ideas.urls')),  # Zastąp 'szkolenia' nazwą swojej aplikacji
    path('custom-admin/edytuj/<int:szkolenie_id>/', views.edytuj_szkolenie, name='edytuj_szkolenie'),
]
