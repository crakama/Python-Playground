from urllib2 import urlopen

# open the API url for reading
openurl = urlopen("http://placekitten.com/200/300")
response = openurl.read()

# limit the response to specific character numbers to control the response
body = response[559:1000]
