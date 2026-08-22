# Di3 – Eigen Docker image experiment (NTP)

Een eigen Docker image (gebaseerd op Alpine Linux) die een NTP-service (chrony) draait om systeemtijd te synchroniseren.

## Inhoud
- `Dockerfile` – image definitie (Alpine + chrony)
- `chrony.conf` – NTP-configuratie

## Uitvoeren
```bash
docker build -t di3-ntp .
docker run -d --name di3-ntp-container di3-ntp
docker exec di3-ntp-container chronyc tracking
```

## Resultaat
Zie screenshot: `di3-ntp-tracking.png`

