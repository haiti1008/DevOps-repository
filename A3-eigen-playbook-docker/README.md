# A3 – Eigen playbook-experiment 2 (Docker)

## Beschrijving
Ansible playbook dat automatisch een nginx Docker-container opstart op poort 8080.

## Gebruikte technologieën
- Ansible
- Docker
- nginx

## Bestanden
- `a3_docker_playbook.yml` – het Ansible playbook

## Uitvoering
```bash
ansible-playbook a3_docker_playbook.yml
```

## Verificatie
```bash
curl http://localhost:8080
```

## Screenshots
- `A3_playbook_run.png` – uitvoer van het playbook
- `A3_verificatie.png` – curl-verificatie van de nginx-container

