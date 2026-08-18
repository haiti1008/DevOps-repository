# Pv2 – Eigen venv-experiment (deployment)

## Doel
Demonstreren hoe een Python virtual environment gebruikt wordt
voor deployment: omgeving opzetten, app schrijven, requirements
exporteren en herdeploy vanuit requirements.txt.

## Gebruikte packages
- Flask
- Requests

## Stappen

### 1. Venv aanmaken en activeren
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Packages installeren
```bash
pip install flask requests
```

### 3. App starten
```bash
python app.py
```
Ga naar: http://localhost:5000

### 4. Requirements exporteren
```bash
pip freeze > requirements.txt
```

### 5. Herdeploy (nieuwe omgeving)
```bash
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Resultaat
De app draait opnieuw identiek na herdeploy vanuit requirements.txt.

