import requests # Need to install
import json
from config import MailChimpConfig

config = MailChimpConfig()

endpoint = 'https://us12.api.mailchimp.com/3.0/batches/39164b3ec6'
response = requests.get(endpoint, auth=('apikey', config.apikey))

#print response.json()

try:
	response.raise_for_status()
	body = response.json()
	print(body)
	id = body['id']
    # Print out new campaign ID to do something else with it (like set content)
    # print(id)
except requests.exceptions.HTTPError as err:
	print('\n\n\nError: %s' % err)

