# J1 – Jenkins Lab 6.3.6: CI/CD Pipeline

Sample-app (Flask) gecommit naar apart GitHub-repo `sample-app`, poort aangepast
naar 5050. Jenkins draait als Docker-container op poort 8080
(`--security-opt seccomp=unconfined` was nodig i.v.m. thread-beperkingen van de VM).

## Jobs
- **BuildAppJob**: haalt code op uit `sample-app` repo en bouwt via `sample-app.sh`
- **TestAppJob**: test of de app antwoordt met curl + grep, draait automatisch na BuildAppJob
- **SamplePipeline**: stopt oude container, bouwt BuildAppJob, bouwt TestAppJob (zie `Jenkinsfile`)

## Bewijs
- `J1-sampleapp-poort5050.png` – app draait op nieuwe poort
- `J1-jenkins-dashboard.png` – Jenkins geconfigureerd
- `J1-alle-jobs-succes.png` – alle drie de jobs succesvol
- `J1-pipeline-stageview.png` – volledige pipeline succesvol

