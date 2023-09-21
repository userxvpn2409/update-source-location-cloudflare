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
domain = 'userxvpn2409.ddns.net'

# Resolve domain
ip_address = resolve_domain(domain)

if ip_address:
    print(f"The IP address of {domain} is: {ip_address}")
else:
    print(f"Failed to resolve the IP address of {domain}")

import requests

account_id = '09e1ce4beeee721da60efa2c06287551'
account_email = 'userxvpn2409@gmail.com'
api_token = '181af2890ac1bea1646afc0cf12a529fd10d8'
uuid = 'c792b4647b374c618db91abd2d17d323'
ip = ip_address + '/32'

url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/locations/{uuid}"

headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
    'X-Auth-Email': account_email,
    'X-Auth-Key': api_token
}

payload = {
    "client_default": True,
    "ecs_support": True,
    "name": "RouterZTE",
    "networks": [
        {
            "network": ip
        }
    ]
}

response = requests.put(url, json=payload, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
