from django import forms
from .models import Szkolenia

class SzkoleniaForm(forms.ModelForm):
    class Meta:
        model = Szkolenia
        fields = ['title', 'date', 'duration', 'available_spots']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'style': 'margin-top: 0px; margin-bottom: 0; width: 200px; height: 20px;'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control', 
                'style': 'margin-top: margin-bottom: 0; 0px; width: 200px; height: 20px;',
            }, format='%Y-%m-%d'),  # Ustawienie formatu daty
            'duration': forms.NumberInput(attrs={
                'class': 'form-control', 
                'style': 'margin-top: 0px; margin-bottom: 0; width: 100px; height: 20px;'
            }),
            'available_spots': forms.NumberInput(attrs={
                'class': 'form-control', 
                'style': 'margin-top: 0px; margin-bottom: 0; width: 100px; height: 20px;'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Automatyczne ustawienie wartości początkowej dla daty
        if self.instance and self.instance.date:
            self.fields['date'].initial = self.instance.date.strftime('%Y-%m-%d')
