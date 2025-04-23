import requests

def load_subdomains(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def try_url(url):
    try:
        response = requests.get(url, timeout=2)
        if response.status_code < 400:
            return True
    except requests.RequestException:
        pass
    return False

def scan_subdomains(domain, wordlist):
    found = []
    for sub in wordlist:
        for scheme in ["https", "http"]:
            url = f"{scheme}://{sub}.{domain}"
            if try_url(url):
                print(f"[+] Found: {url}")
                found.append(url)
                break  
    return found

if __name__ == "__main__":
    target = input("Enter target domain (e.g. example.com): ")
    wordlist = load_subdomains("subdomains.txt")  # you can replace this with other subdomain wordlists 
    results = scan_subdomains(target, wordlist)

    print("\n--- Discovered Subdomains ---")
    for r in results:
        print(r)
