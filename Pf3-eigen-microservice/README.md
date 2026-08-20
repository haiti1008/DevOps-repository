# Pf3 – Eigen microservice-experiment

## Beschrijving
Een eenvoudige Flask-microservice die wiskundige berekeningen uitvoert via HTTP GET-requests.
De service heeft één verantwoordelijkheid: rekenen (add, subtract, multiply, divide).

## Gebruikte technologieën
- Python 3
- Flask

## Bestanden
- microservice.py – Flask-applicatie (calculator microservice)

## Endpoints
| Methode | URL                                      | Beschrijving              |
|---------|------------------------------------------|---------------------------|
| GET     | /health                                  | Statuscheck van de service|
| GET     | /calculate?operation=add&a=5&b=3         | Optelling                 |
| GET     | /calculate?operation=subtract&a=10&b=3   | Aftrekking                |
| GET     | /calculate?operation=multiply&a=6&b=7    | Vermenigvuldiging         |
| GET     | /calculate?operation=divide&a=20&b=4     | Deling                    |

## Starten
python3 microservice.py

## Testen
curl -s http://localhost:5000/health
curl -s "http://localhost:5000/calculate?operation=add&a=10&b=5"

## Screenshots
- Pf3_server_gestart.png
- Pf3_curl_tests.png

