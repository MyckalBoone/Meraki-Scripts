import requests

# Get organizations

url = "https://api.meraki.com/api/v1/organizations"

Headers = [X-CISCO-MERAKI-API-KEY : "Enter key here -> 12293823427447552742319"],

[accept : application/json]

response = requests.request("GET", url, headers=headers)
    print(response.text)

# Get networks from specific organization

url = "https://api.meraki.com/api/v1/organizations/SPECIFIC ORGANIZATION HERE/networks"

Headers = [X-CISCO-MERAKI-API-KEY : "Enter key here -> 12293823427447552742319"],

[accept : application/json]

response = requests.request("GET", url, headers=headers)
    print(response.text)

# Get devices from the specifc network

url = "https://api.meraki.com/api/v1/networks/SPECIFIC NETWORK HERE/devices"

Headers = [X-CISCO-MERAKI-API-KEY : "Enter key here -> 12293823427447552742319"],

[accept : application/json]

response = requests.request("GET", url, headers=headers)
    print(response.text)

