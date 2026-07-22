# 🎯 DealHunterApp

Lekki, modułowy bot do monitorowania platform ogłoszeniowych (Vinted) w czasie rzeczywistym, zintegrowany z powiadomieniami na Discordzie.

## 🛠️ Stos technologiczny
* **Język:** Python 3.13+
* **Zarządzanie pakietami:** `uv`
* **Bezpieczeństwo i sieć:** `curl_cffi`, `playwright` (omijanie Cloudflare L7)
* **Powiadomienia:** Discord Webhooks

## 🚀 Funkcjonalności
* Automatyczne omijanie zabezpieczeń Cloudflare (JS Challenge + TLS Fingerprinting).
* Pobieranie danych bezpośrednio z ukrytych endpointów API Vinted.
* Filtrowanie ofert po cenie u źródła.
* Wyciąganie szczegółowego stanu przedmiotu (np. stan, cena, link).
* Bezpieczna obsługa sekretów za pomocą zmiennych środowiskowych (`.env`).

## ⚙️ Uruchomienie projektu
1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/8B4art3ek/dealhunter.git](https://github.com/8B4art3ek/dealhunter.git)
   cd dealhunter
1. Skonfiguruj plik środowiskowy `.env` w głównym katalogu:
   ```env
   DISCORD_WEBHOOK_URL=Twój_Link_Do_Webhooka
1. Zainstaluj zależności i uruchom aplikację za pomocą `uv` :
   ```bash
   uv sync
   playwright install chromium
   py main.py
