import requests

response = requests.get('https://reqres.in/api/users')
print(type(response))
print(response)