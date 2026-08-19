# Ap5 – Eigen REST-API experiment met curl

## Beschrijving
Een eenvoudige REST API gebouwd met Python Flask voor een takenlijst (tasks).
Alle eindpunten worden getest via curl-commando's.

## Gebruikte technologieën
- Python 3 / Flask
- curl

## Endpoints

| Methode | URL             | Beschrijving         |
|---------|-----------------|----------------------|
| GET     | /tasks          | Alle taken ophalen   |
| GET     | /tasks/<id>     | Één taak ophalen     |
| POST    | /tasks          | Nieuwe taak aanmaken |
| PUT     | /tasks/<id>     | Taak bijwerken       |
| DELETE  | /tasks/<id>     | Taak verwijderen     |

## Server starten
```bash
python3 app.py
```

## Screenshots
- `Ap5_GET_all_tasks.png` – GET alle taken
- `Ap5_GET_single_task.png` – GET één taak
- `Ap5_POST_task.png` – POST nieuwe taak
- `Ap5_PUT_task.png` – PUT taak bijwerken
- `Ap5_DELETE_task.png` – DELETE taak verwijderen
