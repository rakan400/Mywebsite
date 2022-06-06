import requests
import json

response = requests.get('http://numbersapi.com/41')
print(response.json())