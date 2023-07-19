import json
import urllib.request
import sys

GEO_IP_API_URL  = 'http://ip-api.com/json/'
IP = sys.argv[1]
# Can be also site URL like this : 'google.com'
IP_TO_SEARCH    = f"{IP}"

# Creating request object to GeoLocation API
req             = urllib.request.Request(GEO_IP_API_URL+IP_TO_SEARCH)
# Getting in response JSON
response        = urllib.request.urlopen(req).read()
# Loading JSON from text to object
json_response   = json.loads(response.decode('utf-8'))
# Print country
print(json_response['country'], json_response['city'], json_response['timezone'])