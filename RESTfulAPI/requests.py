from urllib2 import urlopen

# Add your code here!
# open the link
website = urlopen("http://placekitten.com/")

# read the data
kittens = website.read()

# Limit the number of characters to be fetched
print kittens[559:1000]	