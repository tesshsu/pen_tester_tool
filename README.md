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
- $ /scan.sh example.com