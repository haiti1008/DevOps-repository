# Dc1 – Run Containers Experiment

Simpel experiment waarbij een nginx-container gestart, getest en opgeruimd wordt.

## Stappen
1. Container starten vanaf de `nginx` image met poortmapping 8082:80
2. Controleren of de container draait (`docker ps`)
3. Webserver testen via `curl localhost:8082`
4. Logs bekijken (`docker logs dc1-nginx`)
5. Container stoppen en verwijderen

## Screenshots
- `docker-ps.png` – container status
- `nginx-test.png` – test van de webserver
- `docker-logs.png` – logoutput van de container

## Opmerking
Poort 8082 gebruikt omdat 8080 en 8081 al bezet waren door andere lopende services (Ansible-nginx en apache2).

