# Pv1 – Python Virtual Environment Lab

## Doel
Demonstratie van het aanmaken, activeren en gebruiken van een Python virtual environment.

## Gebruikte commando's
- `python3 -m venv venv` – aanmaken van de venv
- `source venv/bin/activate` – activeren
- `pip install requests Pillow` – packages installeren
- `pip freeze > requirements.txt` – dependencies vastleggen
- `deactivate` – venv afsluiten

## Bestanden
- `venv_demo.py` – testscript dat requests en Pillow gebruikt
- `requirements.txt` – lijst van geïnstalleerde packages
- `.gitignore` – sluit de venv-map uit van versiebeheer

## Resultaat
Script maakt verbinding met httpbin.org en toont Python- en pakketversies.

