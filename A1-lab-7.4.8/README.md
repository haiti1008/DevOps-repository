# A1 – Lab 7.4.8: Ansible – Apache webserver automatisering

## Beschrijving
Ansible gebruiken om automatisch een Apache2 webserver te installeren en te configureren op een lokale VM via een dummy IPv4-adres (192.0.2.3).

## Bestanden
- `hosts` – Ansible inventory met het webserver-IP en logingegevens
- `ansible.cfg` – Ansible configuratiebestand
- `test_apache_playbook.yaml` – Test-playbook (echo commando)
- `install_apache_playbook.yaml` – Installeert Apache2 op poort 80
- `install_apache_options_playbook.yaml` – Installeert Apache2 op poort 8081

## Resultaat
Apache2 draait op poort 8081 en is bereikbaar via `192.0.2.3:8081` in de browser.

## Gebruikte tools
- Ansible
- SSH / sshpass
- Apache2

