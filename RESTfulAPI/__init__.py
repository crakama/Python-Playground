"""
   An API, or application programming interface,
   is kind of like a coding contract:
   it specifies the ways a program can interact with an application

   For an API or web service to be RESTful, it must do the following:

   1. Separate the client from the server

   2. Not hold state between requests
      (meaning that all the information necessary to respond to a request
      is available in each individual request; no data, or state,
      is held by the server from request to request)

   3. Use HTTP and HTTP methods
"""
from urllib2 import urlopen

# A call to placekitten API
kittens = urlopen('http://placekitten.com/200/300')

f = open('kittens.jpg', 'wb')
f.write(kittens.read())
f.close()
