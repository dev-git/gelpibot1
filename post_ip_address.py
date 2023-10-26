import requests
import datetime;

headers = {
    'Content-Type': 'application/json',
}

def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address
 
# Call the function to get the IP address
ip = get_ip_address()
ct = datetime.datetime.now()

#print("current time:-", ct)
print("IP Address:", ip)

json_data = {
    'ipAddress': ip,
    'created': ct.strftime("%Y-%m-%dT%H:%M:%SZ"),
}

response = requests.post(
    'https://getpantry.cloud/apiv1/pantry/85e96826-af75-4f67-a71e-8b714ee194d3/basket/GELpibot2',
    headers=headers,
    json=json_data,
)
