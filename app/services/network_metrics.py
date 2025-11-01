from typing import Optional
import logging
import socket
import os


logger = logging.getLogger(__name__)

def get_hostname() -> Optional[str]:
    """ Zwraca nazwę hosta"""
    try:
       return socket.gethostname()
    except Exception as e:
        logger.warning(f'Nie udało sie pobrać nazwy hosta: {e}')
        return None
    
    
def get_ip_address() -> Optional[str]:
    """ Zwraca adres IP hosta"""
    try:  
        ip = os.popen("hostname -I").read().strip().split()[0]
        return ip
    except Exception as e:
        logger.warning(f'Nie udało sie pobrać adresu IP: {e}')
        return None


def get_network_info():
    return {
        "hostname": get_hostname(),
        "ip": get_ip_address()
    }