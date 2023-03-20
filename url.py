import requests

from requests.auth import HTTPBasicAuth

response = requests.get('https://instagram.com/',auth = HTTPBasicAuth('7019668173','asfdevil9048'))
print(response)

