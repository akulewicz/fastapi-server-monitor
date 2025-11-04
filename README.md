# FastAPI Server Monitor

![Dashboard](docs/dashboard.png)

**FastAPI Server Monitor** to aplikacja do monitorowania serwera i środowiska systemowego, oferująca prosty dashboard w przeglądarce.  
Umożliwia podgląd temperatury CPU, użycia pamięci i dysku, informacji o systemie, użytkownikach oraz danych z czujnika **BME280** podłączonego do Raspberry Pi.

## Funkcjonalności

- **CPU** – marka, architektura, bity, temperatura  
- **Pamięć RAM** – całkowita, użycie, procent  
- **Dysk** – całkowita pojemność, użycie, procent  
- **System** – nazwa systemu, dystrybucja, wersja  
- **Network** – nazwa hosta, adres IP  
- **Raspberry Pi (opcjonalnie)** – temperatura, wilgotność, ciśnienie w serwerowni  
- **Użytkownicy** – lista aktualnie podłączonych użytkowników  
- **Dashboard** – automatyczna aktualizacja danych co kilka sekund 

## Dane środowiskowe z Raspberry Pi



Aby serwer FastAPI mógł odbierać dane środowiskowe (temperatura, wilgotność, ciśnienie), potrzebna jest aplikacja działająca na Raspberry Pi z czujnikiem **BME280**.

Kod źródłowy klienta dostępny tutaj:  
👉 [rpi-bme280-env-monitor](https://github.com/akulewicz/rpi-bme280-env-monitor)

## Instalacja

### Pobranie repozytorium

Sklonuj projekt z GitHuba:

```bash
git clone https://github.com/akulewicz/fastapi-server-monitor.git
cd fastapi-server-monitor
```

Jeśli zamierzasz korzystać z danych z czujnika BM-280 podłączonego z Raspberry Pi wykonaj:

```bash 
mv app/.env.example app/.env
```

W pliku ```app/.env``` wpisz adres IP i port Raspberry Pi.


### Instalacja za pomocą skryptu Bash

W repozytorium znajduje się skrypt instalacyjny install.sh, który:

- instaluje wymagane pakiety Pythona,
- konfiguruje środowisko wirtualne (venv),
- uruchamia aplikację.

Uruchom skrypt:

```bash
chmod +x install.sh
sudo ./install.sh
```

## API

```bash GET /api/status```

Zwraca wszystkie dane systemowe i środowiskowe w formacie JSON.

**Przykład odpowiedzi:**

```json
{
  "cpu": {"brand": "Intel Core i3", "bits": 64, "arch": "x86_64", "temp": 55.3},
  "memory": {"total": 16777216, "used": 4390912, "percent": 27.7},
  "disk": {"total": 512000000, "used": 240000000, "percent": 46.8},
  "system": {"system": "Linux", "release": "6.1.0", "distro": "Ubuntu 22.04.3 LTS"},
  "network": {"hostname": "my-server", "ip": "192.168.1.10"},
  "env": {"temperature": 23.4, "humidity": 45.2, "pressure": 1013.2},
  "users": {"connected_users": [{"name": "kula", "host": "pts/0"}]}
}

```