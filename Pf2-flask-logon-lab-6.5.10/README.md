# Pf2 – Flask Logon-page Experiment (Lab 6.5.10)

## Beschrijving
Flask webservice die de evolutie van wachtwoordopslag demonstreert.
Versie 1 slaat wachtwoorden op als plaintext in een SQLite-database.
Versie 2 slaat wachtwoorden op als SHA256-hash.

## Gebruikte technologieën
- Python 3
- Flask
- SQLite3
- hashlib (SHA256)
- pyotp
- curl

## Hoe uitvoeren

### Server starten
```bash
nohup python3 password-evolution.py &
```

### Plaintext signup/login
```bash
curl -k -X POST -F 'username=alice' -F 'password=myalicepassword' 'https://0.0.0.0:5000/signup/v1'
curl -k -X POST -F 'username=alice' -F 'password=myalicepassword' 'https://0.0.0.0:5000/login/v1'
```

### Hash signup/login
```bash
curl -k -X POST -F 'username=rick' -F 'password=samepassword' 'https://0.0.0.0:5000/signup/v2'
curl -k -X POST -F 'username=rick' -F 'password=samepassword' 'https://0.0.0.0:5000/login/v2'
```

### Server stoppen
```bash
pkill -f password-evolution.py
```

## Bestanden
- `password-evolution.py` – Flask applicatie
- `screenshots/` – Schermafbeeldingen van de uitvoering

