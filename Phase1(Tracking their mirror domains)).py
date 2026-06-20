#code for crt.sh automation
import requests
import json

def fetch_ct_logs(search_query):
    print(f"[*] Querying crt.sh for: {search_query}...")
    url = f"https://crt.sh/?q={search_query}&output=json"
    
    try:
        response = requests.get(url, timeout=20)
        if response.status_code == 200:
            data = response.json()
            
            # Use a set to keep only unique domain names
            unique_domains = set()
            for entry in data:
                # Remove wildcard notation if present
                domain = entry['name_value'].replace('*.', '')
                unique_domains.add(domain)
            
            print(f"[+] Found {len(unique_domains)} unique domains matching signature!\n")
            
            # Print the first 20 discovered mirrors as a sample
            for i, domain in enumerate(sorted(unique_domains)):
                if i < 20:
                    print(f"  [-] Discovered Mirror: {domain}")
                else:
                    print(f"  ... and {len(unique_domains) - 20} more.")
                    break
        else:
            print(f"[-] Error: Received status code {response.status_code}")
    except Exception as e:
        print(f"[-] Request failed (crt.sh might be rate-limiting or overloaded): {e}")

if __name__ == "__main__":
    # Look for sequential patterns commonly used by gambling platforms
    fetch_ct_logs("%1xbet%")
