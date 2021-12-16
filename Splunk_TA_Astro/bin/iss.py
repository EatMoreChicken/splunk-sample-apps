# The Requests library allows Python to make HTTP Requests.
# In this example, the request will be to API endpoints
# Requests Documentation: https://docs.python-requests.org/en/latest/
import requests
import json

# Variables
base_url='http://api.open-notify.org/iss-now.json'

# Get Request to the base_url
r = requests.get(base_url)

# Printing the output
print(json.dumps(r.json()))