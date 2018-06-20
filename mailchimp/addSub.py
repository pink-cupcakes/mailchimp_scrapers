# This example shows a basic POST request to create a new campaign
# See below, there are several variables you need to update

import requests # Need to install
import json
from config import MailChimpConfig

config = MailChimpConfig()

mailchimp_list_id = '4a60ee669f'
path = "lists/" + mailchimp_list_id + "/members/"

# path = "campaigns"
endpoint = config.api_root + path

# Create metadata for campaign
# See: http://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/
meta = {}

meta['email_address'] = 'winnie@cooper.com'

meta['status'] = 'subscribed'

meta['merge_fields'] ={
    'FNAME' : 'Winnie',
    'LNAME' : 'Yu',
    'END1': '03/25/2018',
    'CLASS1':'LCI',
    'CLASS1CITY':'New York'
}

#print meta

# JSON-ify metadata
payload = json.dumps(meta)

#print payload

# Send  post request
response = requests.post(endpoint, auth=('apikey', config.apikey), data=payload)

#print response.json()

try:
    response.raise_for_status()
    body = response.json()
    id = body['id']
    # Print out new campaign ID to do something else with it (like set content)
    print(id)
except requests.exceptions.HTTPError as err:
    print('\n\n\nError: %s' % err) 
