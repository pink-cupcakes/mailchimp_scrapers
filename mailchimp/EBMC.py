#================================
# Import Event Brite Libraries
#================================
import time
from eventbrite import Eventbrite

#================================
# Import Mailchimp Libraries
#================================
import requests # Need to install
import json
from config import MailChimpConfig


#================================
# Authorize Eventbrite & Mailchimp
#================================

#EventBrite
eventbrite = Eventbrite('D6P5CGYEQMZQXPBSPJDG')
user = eventbrite.get_user()  # Not passing an argument returns yourself
# Get my own User ID
my_id = eventbrite.get_user()['id']

#Mailchimp Gets configured: then it is authorized during each post request
config = MailChimpConfig()

#================================
# Define List ID's for different Lists in MChimp
#================================

# Define Additional List ID's here
#

mailchimp_list_id = '4a60ee669f'
path = "lists/" + mailchimp_list_id + "/members/"

# path = "campaigns"
endpoint = config.api_root + path

#=====================
# Get the current date
#=====================
today = time.strftime("%Y-%m-%d")
print (time.strftime("%Y-%m-%d"))


#===============================
# Get all of my event id numbers
#===============================
events = eventbrite.event_search(**{'user.id': my_id})
print(events)
# HOW many events are there
total_events =  events['pagination']['object_count']

# For the total number of events return an array of their id numbers -(Add later if too many people)(If the events are still live)
eventid=[total_events]
for a in range(0,total_events-1):
        print(a)
        eventid[a] = events['events'][a]['id']
        print(eventid[a])
#=============================
# For each event get all eventbrite attendees
# if they signed up today, add their registration id to a list
#=============================
register_today = []

for y in eventid:
	# Get the data for the specific Event
	eventInfo = eventbrite.get('/events/'+y+'/')
	print(eventInfo)
	EventName = eventInfo['name']['text']
	EndDate = eventInfo['end']['local']

	venue = eventInfo['venue_id']
	# I need to figure out how to get the event location if one exists

	city = eventbrite.get('/venues/'+venue+'/')
	print(city)

	# Get Info on each Attendee
	attend = eventbrite.get('/events/'+y+'/attendees/')

	#print(attend)
	print('\n')
	#attend = eventbrite.get('/events/34072776592/attendees/') 34072776592

	count = attend['pagination']['object_count']
	items = attend['attendees']

	for x in range(0,count):
		email = items[x-1]['profile']['email']
		firstName = items[x-1]['profile']['first_name']
		lastName = items[x-1]['profile']['last_name']



		created = items[x-1]['created']
		print(email + ' ' + created[0:10])
		#=====================================
		# Compare the date created; if today - act
		#=========================================
		if today == created[0:10]:
			print('created today')
			#hello =  items[x-1]['event_id']
			register_today.append(items[x-1]['order_id'])
			print(register_today)
