import requests

def resolve_domain(domain):
    api_url = 'https://dns.google.com/resolve'
    query_params = {
        'name': domain,
        'type': 'A'
    }
    
    response = requests.get(api_url, params=query_params)
    data = response.json()
    
    if 'Answer' in data and isinstance(data['Answer'], list) and len(data['Answer']) > 0:
        ip_addresses = [answer['data'] for answer in data['Answer'] if answer['type'] == 1]
        return ip_addresses[0] if ip_addresses else None
    else:
        return None

# Domain name to resolve
domain = 'cc220ed01053.sn.mynetname.net'

# Resolve domain
ip_address = resolve_domain(domain)

if ip_address:
    print(f"The IP address of {domain} is: {ip_address}")
else:
    print(f"Failed to resolve the IP address of {domain}")
