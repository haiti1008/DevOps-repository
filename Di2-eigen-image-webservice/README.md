# Di2 – Eigen Docker image experiment (webservice)

Een eenvoudige Flask webservice, gecontaineriseerd met een eigen Docker image.

## Inhoud
- `app.py` – Flask applicatie
- `requirements.txt` – Python dependencies
- `Dockerfile` – image definitie

## Uitvoeren
```bash
docker build -t di2-webservice .
docker run -d -p 5000:5000 --name di2-container di2-webservice
curl http://localhost:5000
```

## Resultaat
Zie screenshot: `di2-docker-curl-test.png`

