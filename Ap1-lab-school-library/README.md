# Ap1 – Lab 4.5.5 School Library experiment

## Doel
Verkennen van een REST API (School Library simulator) via de API-documentatie, Postman en Python.

## Gebruikte tools
- Chromium (API-documentatie / Swagger UI)
- Postman
- Python 3 (requests, faker)

## Stappen
1. API-documentatie bekeken op `library.demo.local/api/v1/docs`
2. In Postman:
   - `GET /api/v1/books` — boekenlijst opgehaald
   - `POST /api/v1/loginViaBasic` — ingelogd (Basic Auth: cisco/Cisco123!) en API-token verkregen
   - `POST /api/v1/books` — nieuw boek toegevoegd met `X-API-KEY` authenticatie
3. Verificatie via `GET /api/v1/books` dat het boek was toegevoegd
4. Python-script `add100RandomBooks.py` uitgevoerd om 100 willekeurige boeken toe te voegen via de Faker-library

## Resultaat
- Boek "Testboek Haitham" succesvol toegevoegd via Postman (status 200)
- 100 extra boeken succesvol toegevoegd via het Python-script
- Zie screenshots: `postman-get-verificatie.png`, `terminal-output-100-boeken.png`, `browser-boekenlijst-bijgewerkt.png`
