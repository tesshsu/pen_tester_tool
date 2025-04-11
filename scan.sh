#!/bin/bash

# Check if a domain name is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

# Assign the domain to a variable
DOMAIN="$1"
OUTPUT_FILE="results/result.txt"

# Validate domain format (basic check)
if ! [[ "$DOMAIN" =~ ^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    echo "Error: Invalid domain format. Please provide a valid domain (e.g., example.com)."
    exit 1
fi

# Create results directory if it doesn't exist
mkdir -p results

# Function to check if a tool is installed
check_tool() {
    if ! command -v "$1" >/dev/null 2>&1; then
        echo "Error: $1 is not installed. Please install it to proceed."
        exit 1
    fi
}

# Check for tee (required for output handling)
check_tool "tee"

# Function to append a header to the output file
append_header() {
    echo "=========================================" >> "$OUTPUT_FILE"
    echo "Scan Results for $DOMAIN - $1" >> "$OUTPUT_FILE"
    echo "=========================================" >> "$OUTPUT_FILE"
}

# Function to run Nmap scan
func_nmap() {
    check_tool "nmap"
    echo "Running Nmap scan on $DOMAIN..."
    append_header "Nmap"
    nmap -A "$DOMAIN" | tee -a "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Function to run SSLScan
func_sslscan() {
    check_tool "sslscan"
    echo "Running SSLScan on $DOMAIN..."
    append_header "SSLScan"
    sslscan "$DOMAIN" | tee -a "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Function to run WhatWeb
func_whatweb() {
    check_tool "whatweb"
    echo "Running WhatWeb on $DOMAIN..."
    append_header "WhatWeb"
    whatweb "$DOMAIN" | tee -a "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Function to run Dirb
func_dirb() {
    check_tool "dirb"
    echo "Running Dirb on $DOMAIN..."
    append_header "Dirb"
    dirb "http://$DOMAIN" | tee -a "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Function to run Nikto
func_nikto() {
    check_tool "nikto"
    echo "Running Nikto on $DOMAIN..."
    append_header "Nikto"
    nikto -h "http://$DOMAIN" | tee -a "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Function to run Amass
func_amass() {
    check_tool "amass"
    echo "Running Amass on $DOMAIN..."
    append_header "Amass"
    amass enum -d "$DOMAIN" | tee -a "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Function to run Sublist3r
func_sublist3r() {
    check_tool "sublist3r"
    echo "Running Sublist3r on $DOMAIN..."
    append_header "Sublist3r"
    sublist3r -d "$DOMAIN" | tee -a "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}


# Function to run theHarvester
func_theharvester() {
    check_tool "theharvester"
    echo "Running theHarvester on $DOMAIN..."
    append_header "theHarvester"
    theharvester -d "$DOMAIN" -b all | tee -a "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Function to run FinalRecon
func_finalrecon() {
    check_tool "finalrecon"
    echo "Running FinalRecon on $DOMAIN..."
    append_header "FinalRecon"
    finalrecon --full "http://$DOMAIN" | tee -a "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Function to run Burp (placeholder)
func_burp() {
    echo "Burp Suite is a manual tool. Please run it separately on $DOMAIN."
    append_header "Burp Suite"
    echo "Burp Suite scan not automated. Run manually." >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Main function to run all scans
run_all_scans() {
    echo "Starting scan on $DOMAIN..."
    echo "Results will be appended to $OUTPUT_FILE"
    echo "=========================================" > "$OUTPUT_FILE"
    echo "Scan Started: $(date)" >> "$OUTPUT_FILE"
    echo "=========================================" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"

    # Run all tools
    func_nmap
    func_sslscan
    func_whatweb
    func_dirb
    func_nikto
    func_amass
    func_sublist3r
    func_theharvester
    func_finalrecon
    func_burp

    echo "=========================================" >> "$OUTPUT_FILE"
    echo "Scan Completed: $(date)" >> "$OUTPUT_FILE"
    echo "=========================================" >> "$OUTPUT_FILE"
    echo "Scan completed. Results saved to $OUTPUT_FILE"
}

# Execute the scans
run_all_scans