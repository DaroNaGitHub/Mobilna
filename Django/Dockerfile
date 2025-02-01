# Wybierz obraz bazowy z Pythona
FROM python:3.10-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj plik wymagań
COPY requirements.txt ./

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj cały projekt do katalogu w kontenerze
COPY . .

# Otwórz port 8000 (domyślny port Django)
EXPOSE 7000

# Polecenie uruchamiające serwer deweloperski Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:7000"]

