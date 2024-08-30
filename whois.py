#!/usr/bin/env python3

import subprocess
import sys
import re

def run_whois(domain):
    try:
        # Run the whois command and capture the output
        result = subprocess.run(['whois', domain], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

def extract_info(whois_data):
    info = {}
    
    # Define patterns for key information
    patterns = {
        'Domain Registrar': r'Registrar:\s*(.*)',
        'Registration Date': r'Creation Date:\s*(.*)',
        'Expiration Date': r'Registry Expiry Date:\s*(.*)',
        'Registrant Name': r'Registrant Name:\s*(.*)',
        'Registrant Organization': r'Registrant Organization:\s*(.*)',
        'Registrant Email': r'Registrant Email:\s*(.*)',
        'Registrant Address': r'Registrant Street:\s*(.*)',
        'Name Server': r'Name Server:\s*(.*)'
    }
    
    # Extract information using the defined patterns
    for key, pattern in patterns.items():
        matches = re.findall(pattern, whois_data, re.IGNORECASE)
        if matches:
            info[key] = matches if key == 'Name Server' else matches[0].strip()
    
    return info

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python whois.py <domain>")
        sys.exit(1)
    
    domain = sys.argv[1]
    
    # Get WHOIS information
    whois_data = run_whois(domain)
    
    if "Error" in whois_data or "Exception occurred" in whois_data:
        print(whois_data)
    else:
        # Extract key information
        info = extract_info(whois_data)
        
        # Print the extracted information
        for key, value in info.items():
            if isinstance(value, list):
                for v in value:
                    print(f"{key}: {v}")
            else:
                print(f"{key}: {value}")
