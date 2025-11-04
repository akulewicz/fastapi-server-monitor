#!/bin/bash
set -e 

PYTHON_BIN=$(which python3)

if [ -z "$PYTHON_BIN" ]
then
    echo "➡️  Python nie jest zainstalowany. Instaluję...."
    sudo apt update && sudo apt install -y python3 python3-venv python3-pip
fi

echo "➡️  Tworzenie środowiska wirtualnego..."
python3 -m venv venv
source venv/bin/activate

echo "➡️  Instalacja zależności..."
pip install --upgrade pip
pip install -r requirements.txt

echo "➡️  Ustawiam uprawnienia do logów..." 
chown -R $USER:$USER logs

echo "➡️  Uruchamiam aplikację. Aby z niej skorzystać wejdź na http://$(hostname -I | awk '{print $1}'):8000"
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
