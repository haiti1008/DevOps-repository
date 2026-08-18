# Ap2-lab-4.9.2

## Doel
Een Python-applicatie bouwen die de Graphhopper REST API gebruikt om een locatienaam om te zetten naar coördinaten (Geocoding) en vervolgens een routebeschrijving op te vragen tussen twee locaties (Routing), inclusief afstand, duur en stap-voor-stap instructies.

## Gebruikte tools
- Python 3 (modules: `requests`, `urllib.parse`)
- Graphhopper Geocoding API & Routing API
- VS Code

## Stappen
1. Geocoding-functie gebouwd die een locatienaam omzet naar lat/lng via de Graphhopper Geocoding API, met foutafhandeling voor ongeldige locaties.
2. Gebruikersinvoer toegevoegd voor start- en bestemmingslocatie, met een `quit`/`q`-optie om te stoppen.
3. Routing-functionaliteit toegevoegd: bouwt een routing-URL op basis van de coördinaten, vraagt de route op, en toont afstand (mijl/km) en duur (hh:mm:ss).
4. Stap-voor-stap routebeschrijving toegevoegd via een `for`-lus over de `instructions`-lijst uit de JSON-data.
5. Foutafhandeling toegevoegd voor ongeldige routes (bv. geen verbinding tussen twee locaties).
6. Keuze van vervoersmiddel toegevoegd (car/bike/foot), met terugval op "car" bij ongeldige invoer.

## Resultaat
De applicatie geeft correct de geocoded locaties, routebeschrijving, afstand en duur weer voor geldige routes, en toont een duidelijke foutmelding bij ongeldige input of onbereikbare routes. Zie screenshots `ap2-4-geocoding-test1` t/m `test7` (opbouw geocoding) en `ap2-5-routing-success` / `ap2-6-routing-error` (routing + foutafhandeling).
