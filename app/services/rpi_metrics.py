from typing import Optional
import requests
import logging

logger = logging.getLogger(__name__)

RPI_API_URL = "http://192.168.1.6:8000/env"  

def get_rpi_env() -> Optional[dict]:
    """Pobiera dane środowiskowe z Raspberry Pi (BME280)."""
    try:
        response = requests.get(RPI_API_URL, timeout=1)
        response.raise_for_status()
        data = response.json()
        return {
            "temperature": round(data.get("temperature"), 1),
            "humidity": round(data.get("humidity"),1 ),
            "pressure": round(data.get("pressure"), 1)
        }
    except requests.RequestException as e:
        logger.warning(f"Nie udało się pobrać danych z RPi: {e}")
        return {}