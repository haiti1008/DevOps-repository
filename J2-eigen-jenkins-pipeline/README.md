# J2 – Eigen Jenkins Pipeline-experiment

Declarative pipeline (`SimpleReportPipeline`) die zelfstandig draait, zonder externe
repo of Docker build. Genereert een rapport, test de inhoud, en archiveert het
resultaat als build-artifact.

## Stages
- **Build**: schrijft build-nummer en datum naar `report.txt`
- **Test**: controleert of `report.txt` het build-nummer bevat
- **Archive**: bewaart `report.txt` als build-artifact via `archiveArtifacts`

## Bewijs
- `J2-pipeline-stageview.png` – alle 3 stages succesvol
- `J2-build-artifact.png` – gearchiveerd rapport zichtbaar op de build-pagina

