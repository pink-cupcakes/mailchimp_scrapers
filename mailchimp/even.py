
#=====================
# Import Eventbrite 
#=====================
import json
import time
from eventbrite import Eventbrite
#WORKS prints the objects inside the eventbrite file             print(dir())

#Authorization
eventbrite = Eventbrite('D6P5CGYEQMZQXPBSPJDG')
user = eventbrite.get_user()  # Not passing an argument returns yourself
#print(user)
# Get my own User ID
my_id = eventbrite.get_user()['id']

#=====================
# Import Mailchimp
#=====================

import requests
from config import MailChimpConfig

config = MailChimpConfig()

mailchimp_list_id = '4a60ee669f'
path = "lists/" + mailchimp_list_id + "/members/"
#If the email is already in the list this line will throw an error 404 not found: Should check if the person is in the list: if so, update them, don't add them
endpoint = config.api_root + path
#print(endpoint)
#=====================
# Get the current date
#=====================
today = time.strftime("%Y-%m-%d")
#print (time.strftime("%Y-%m-%d"))


#===============================
# Get all of my event id numbers
#===============================
events = eventbrite.event_search(**{'user.id': my_id})

# HOW many events are there
total_events =  events['pagination']['object_count']
#print(total_events)

#print(events['events'])
# For the total number of events return an array of their id numbers -(Add later if too many people)(If the events are still live)
eventid=[]

# Dictionary to store todays purchasers json data inside
data = 	{}
place = 0
for x in range(0,total_events-1):
#	print(x)
	eventid.append(events['events'][x]['id'])
#	print(eventid[x])
#=============================
# For each event get all eventbrite attendees
# if they signed up today, add their registration id to a list
#=============================
register_today = []


for y in eventid:
	#Get event information
	eventInfo = eventbrite.get('/events/'+y+'/')
	eventName = eventInfo['name']['text']
	endd = eventInfo['end']['local']
	endDate = endd[5:7]+'/'+endd[8:10]+'/'+endd[0:4]
#	print(endDate)	#mm/dd/yyyy
	eventLocation = eventInfo['end']['timezone']

	#Get all of the attendees for this event
	attend = eventbrite.get('/events/'+y+'/attendees/') # print(attend)
	count = attend['pagination']['object_count']
	items = attend['attendees']
	for x in range(0,count):
		#=========================================
                # Compare the date created; if today - act
                #=========================================
		created = items[x-1]['created']
		email = items[x-1]['profile']['email']
#		print(email + ' ' + created[0:10])
		today2 = '2017-04-28'
		if today2 == created[0:10]:
#			print('created today') 
			#GET the rest of the users information
			first = items[x-1]['profile']['first_name']
			last = items[x-1]['profile']['last_name']
			#===============================
			# Create a Json object and add it to the master dictionary
			#===============================

#Put in the form to be accepted by the PUT command

			meta = {}
			meta['email_address'] = email
			meta['status'] = 'subscribed' #always subscribed
			meta['merge_fields'] = {
				'FNAME' : first, #'Winnie',
				'LNAME' : last,
				'END1' : endDate,
				'CLASS1' : eventName,
				'CLASS1CITY' : eventLocation
			}
			#json-ify meta data & add it to the json array
			data[place] = meta
			place = place+1;
			#		json_data.append(meta)
			#add the payload to the json dictionary todaysPurchases
			#todaysPurchases.append(payload)

# Write the final Json Array to a text file
with open('subscribers.json', 'w') as outfile:
    json.dump(data, outfile)






# Can create a new user in mailchimp
# Might be better in Bash
# Especially for future mailchimp manipulations
#
#			response = requests.post(endpoint, auth=('apikey',config.apikey), data=payload)
#			#print the response
#			try:
#				response.raise_for_status()
#				body = response.json()
#				id = body['id']
#				print(id)
#			except requests.exceptions.HTTPError as err:
#				print('\n\n\nError: %s'  % err)


