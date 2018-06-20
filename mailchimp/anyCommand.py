# This example shows a basic POST request to create a new campaign
# See below, there are several variables you need to update

import requests # Need to install
import json
from config import MailChimpConfig

config = MailChimpConfig()



path = "batches"
endpoint = config.api_root + path
#print(endpoint)

# Create metadata for campaign
# See: http://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/


# Create the users here:
user = {}
user["email_address"] ="oates@hallandoates.com"
user["status_if_new"] ="subscribed"

# Create a data scructure here :
meta =  {
	"operations": [
	{
	"method":"PUT",
	"path": "lists/4a60ee669f/members/ad2a82f647b25de3135c59acd2806263",
	"body":user
	}
	]
	}

meta2 ={
	"operations": [
	{
        "method":"PUT",
        "path": "lists/4a60ee669f/members/ad2a82f647b25de3135c59acd2806263",
        "body":'{"email_address":"oates@hallandoates.com","status":"subscribed"}'
        }
	]
	}

meta3 ={
        "operations": [
        {
        "method":"PUT",
        "path": "lists/4a60ee669f/members/ad2a82f647b25de3135c59acd2806263",
        "body":"{\"email_address\":\"oates@hallandoates.com\",\"status\":\"subscribed\"}"
        }
        ]
        }

# Write the data structure to mailchimp
# JSON-ify metadata
#payload = json.dumps(meta2)
#print(payload)

# Send  post request

payload = json.dumps(user)
print(payload)
path2 = config.api_root + 'lists/4a60ee669f/members/ad2a82f647b25de3135c59acd2806263'
response = requests.put(path2, auth=('apikey', config.apikey), data=payload)
#response = requests.post(endpoint, auth=('apikey', config.apikey), data=payload)

#print response.json()

try:
    response.raise_for_status()
    body = response.json()
    id = body['id']
    # Print out new campaign ID to do something else with it (like set content)
    print(id)
except requests.exceptions.HTTPError as err:
	print('\n\n\nError: %s' % err)
