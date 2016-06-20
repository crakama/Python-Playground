"""
The 4 verbs are:

GET: retrieves information from the specified source.
POST: sends new information to the specified source.
PUT: updates existing information of the specified source.
DELETE: removes existing information from the specified source.

another way to communicate through HTTP is with the requests library

"""
import requests

# Make a GET request here and assign the result to kittens:

kittens = requests.get("http://placekitten.com/")
print kittens.text[559:1000]
