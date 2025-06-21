import requests

token = "REDCAP_API_TOKEN"
url = "https://redcap.ucsf.edu/api/"
payload = {
    'token': token,
    'content': 'record',
    'format': 'json',
    'type': 'flat'
}

response = requests.post(url, data=payload)
records = response.json()
df = pd.DataFrame(records)
