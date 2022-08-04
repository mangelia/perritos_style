from urllib import request
import requests
import json

r = requests.get("https://dog.ceo/api/breeds/image/random")
print(type(r))
otra_variable = json.loads(r.text)

print(otra_variable, type(otra_variable))

print(r.text, type(r.text))

print(otra_variable["message"])
