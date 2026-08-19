# Ap6 – Eigen REST-API experiment met curl (Forms)

## Beschrijving
Een Flask REST API die form-data verwerkt via curl.  
Studenten kunnen worden toegevoegd, bekeken, aangepast en verwijderd
via `application/x-www-form-urlencoded` form-data.

## Endpoints

| Method | URL                  | Beschrijving              |
|--------|----------------------|---------------------------|
| GET    | /students            | Alle studenten ophalen    |
| GET    | /students/<id>       | Één student ophalen       |
| POST   | /students            | Nieuwe student toevoegen  |
| PUT    | /students/<id>       | Student updaten           |
| DELETE | /students/<id>       | Student verwijderen       |

## Gebruikte technologieën
- Python 3 / Flask
- curl (form-data via `-d`)

## Uitvoering
```bash
python3 app.py
```

## Curl-commando's (voorbeelden)
```bash
curl -X POST http://localhost:5000/students -d "name=Alice&email=alice@example.com&course=DevACS"
curl -X GET  http://localhost:5000/students
curl -X PUT  http://localhost:5000/students/1 -d "course=DevNet+Associate"
curl -X DELETE http://localhost:5000/students/1
```

## Screenshots
- Ap6_01_flask_running.png
- Ap6_02_post_students.png
- Ap6_03_get_all.png
- Ap6_04_get_one_and_put.png
- Ap6_05_delete_and_verify.png

