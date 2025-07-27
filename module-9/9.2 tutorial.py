import requests
import json 

response = requests.get("http://api.open-notify.org/astros") 
print(response.status_code)


def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())

response = requests.get("https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa") 
data = response.json()