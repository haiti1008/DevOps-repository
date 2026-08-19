# Ap4 – Eigen API-experiment met Python Webforms

## Beschrijving
Een Flask-webapplicatie waarmee je via HTML-formulieren (webforms) Cisco-netwerkapparaten kunt beheren.  
De app biedt zowel een webinterface als een JSON API-endpoint.

## Functionaliteit
- Apparaten toevoegen via webform (hostname, IP, type)
- Apparaten verwijderen via de webpagina
- JSON API-endpoint: `GET /api/devices`

## Bestanden
| Bestand | Functie |
|---|---|
| `app.py` | Flask-applicatie met routes |
| `templates/index.html` | HTML-webpagina met formulier en tabel |

## Hoe uitvoeren
```bash
python3 app.py
```
Daarna: open `http://localhost:5000` in de browser.

## API
| Route | Methode | Beschrijving |
|---|---|---|
| `/` | GET | Webpagina met formulier en lijst |
| `/add` | POST | Apparaat toevoegen via form |
| `/delete/<id>` | POST | Apparaat verwijderen |
| `/api/devices` | GET | Alle apparaten als JSON |

## Screenshots
- `Ap4_01_webform_devices.png` – Webpagina met apparaten
- `Ap4_02_device_deleted.png` – Na verwijdering
- `Ap4_03_api_json.png` – JSON API-response

