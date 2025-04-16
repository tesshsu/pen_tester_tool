# Pen Tester Tool

A Bash script designed for penetration testers to perform basic reconnaissance and vulnerability scanning on a target domain. The script automates the use of multiple tools and appends their results to a single output file for easy analysis.

## Features
- Takes a domain name as input and performs scans using various tools.
- Outputs results to `results/result.txt` with clear formatting and timestamps.
- Includes error handling for missing tools and invalid domain formats.
- Supports the following tools:
  - **SSLScan**: Scans for SSL/TLS vulnerabilities.
  - **WhatWeb**: Identifies domain name, IP, cookies, and server information.
  - **Amass**: Performs subdomain enumeration.
  - **Nmap**: Conducts network exploration and port scanning.
  - **Dirb**: Enumerates directories and files on a web server.
  - **Nikto**: Scans for web server vulnerabilities.
  - **Sublist3r**: Enumerates subdomains of the target domain.
  - **theHarvester**: Gathers emails, subdomains, hosts, and other information.
  - **FinalRecon**: Performs a comprehensive reconnaissance scan.
  - **Burp Suite**: Placeholder for manual scanning (not automated).

## Prerequisites
Ensure the following tools are installed on your system:
- `nmap`
- `sslscan`
- `whatweb`
- `dirb`
- `nikto`
- `amass`
- `sublist3r`
- `theharvester`
- `finalrecon`

### Installation Instructions
1. **Install the tools**:
   On a Debian-based system (e.g., Kali Linux, Ubuntu), you can install most tools using `apt`. For example:
   ```bash
   sudo apt update
   sudo apt install nmap sslscan whatweb dirb nikto

### Usage
- $ chmod +x scan.sh
- $ ./scan.sh example.com
- For payload sqli copy the query and attach like any path query like 'GET /rest/products/search?q=')) union select 1,2,3,4,5,6,7,8,name from sqlite_master where type='table'-- HTTP/1.1'

### Usage for basic python scan web TOP OWASP
python_scan/
├── scan.py
├── liste.txt
└── .env

- $ pip install requests python-dotenv
- edit .env file which site url you want to scan
- $ python3 scan.py

## PS
- If you need to copy code in windows system from unix Linux sytem need to change system from LF to CRLF



# 🔐 Rapport de Pentest – Fiches de Vulnérabilités

## 📁 Exemple de Fiche de Vulnérabilité

---

### ✅ 1. Type de faille
- **Nom** : XSS réfléchi
- **Description** :
  Une faille XSS de type « Réfléchi » a été découverte dans le champ de recherche du site web. Cela permet à un attaquant d’injecter du code JavaScript dans les pages, ce qui peut notamment mener à du vol de cookies dans certains cas.  
  La portée de l'attaque est relativement limitée par la nature même de la vulnérabilité.

---

### 🧨 2. Score CVSS
- **Score CVSS** : 6.9
- **Vecteur CVSS** : `AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N/E:P/RL:O/RC:C`

---

### 🧩 3. Identifiants
- **CVE concernée** : _non assignée_
- **CWE principale** : `CWE-79` – Improper Neutralization of Input During Web Page Generation
- **CWE complémentaire** : `CWE-912` – Hidden Functionality (si applicable)

---

### 🧪 4. Reproduction de l'exploit
- **Lien de test** :  
  `http://ip.to-21-112-5/search.php?query=%3Cscript%3Ealert(1)%3C/script%3E`

- **Payload utilisé** :
  ```html
  <script>alert('XSS')</script>
