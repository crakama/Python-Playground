### ANATOMY OF REQUEST ###
############ Request line #############
# POST /learn-http HTTP/1.1
"""
which tells the server what kind of request is being sent (GET, POST, etc.) and what resource it's looking for
"""


############## Header ################
# Host: www.codecademy.com
# Content-Type: text/html; charset=UTF-8
"""
 which sends the server additional information (such as which client is making the request
"""

############### Body #################
# Name=Eric&Age=26
"""
which can be empty (as in a GET request) or contain data (if you're POSTing or PUTing information, that information is contained here
"""
