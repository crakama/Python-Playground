import requests

response = requests.get('http://placekitten.com/')

# Add your code below!
code = response.status_code
print code