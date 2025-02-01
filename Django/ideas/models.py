from django.db import models
from django.contrib.auth.models import User

IDEA_STATUS = (
    ('pending', 'Czekam na recenzję'),
    ('accepted', 'Przyjęty'),
    ('rejected', 'Odrzucony')

)

class Idea(models.Model):
    title = models.CharField(max_length=255)
    descripton = models.TextField()
    youtube_url = models.URLField(null=True, blank=True)
    status = models.CharField(choices = IDEA_STATUS, max_length=30, default='pending')

    def __str__(self):
        return self.title

class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f'id {self.id}' 
    
class Szkolenia(models.Model):
    title = models.CharField(max_length=300, verbose_name="Tytuł szkolenia")  # Tytuł ogłoszenia
    date = models.DateField(verbose_name="Data szkolenia")  # Data
    duration = models.PositiveIntegerField(verbose_name="Czas trwania (dni)")  # Czas trwania (np. w dniach)
    available_spots = models.PositiveIntegerField(verbose_name="Wolne miejsca")  # Ilość wolnych miejsc (tylko liczby dodatnie)

    def __str__(self):
        return self.title  # Wygodny sposób reprezentacji obiektu jako tekst
    
    
class Zapis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    szkolenie = models.ForeignKey(Szkolenia, on_delete=models.CASCADE)
    zapis_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} zapisany na {self.szkolenie.title}"

