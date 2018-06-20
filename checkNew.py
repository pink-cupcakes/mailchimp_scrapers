#=====================
# Import Eventbrite 
#=====================
import time
from eventbrite import Eventbrite
#WORKS prints the objects inside the eventbrite file             print(dir())

#Authorization
eventbrite = Eventbrite('D6P5CGYEQMZQXPBSPJDG')
user = eventbrite.get_user()  # Not passing an argument returns yourself
# Get my own User ID
my_id = eventbrite.get_user()['id']

#=====================
# Import Mailchimp
#=====================

#import requests
#import json
#from config import MailChimpConfig

#=====================
# Get the current date
#=====================settings
today = time.strftime("%Y-%m-%d")
print (time.strftime("%Y-%m-%d"))


#===============================
# Get all of my event id numbers
#===============================
events = eventbrite.event_search(**{'user.id': my_id})

# HOW many events are there
total_events =  events['pagination']['object_count']
print(total_events)

#print(events['events'])
# For the total number of events return an array of their id numbers -(Add later if too many people)(If the events are still live)
eventid=[]

for x in range(0,total_events-1):
	print(x)
	eventid.append(events['events'][x]['id'])
	print(eventid[x])
#=============================
# For each event get all eventbrite attendees
# if they signed up today, add their registration id to a list
#=============================
register_today = []

for y in eventid:
	eventInfo = eventbrite.get('/events/'+y+'/')
	print(eventInfo)
	attend = eventbrite.get('/events/'+y+'/attendees/')
	#print(attend)
	print('\n')
	#attend = eventbrite.get('/events/34072776592/attendees/') 34072776592

	count = attend['pagination']['object_count']
	items = attend['attendees']

	for x in range(0,count):
		email = items[x-1]['profile']['email']
		created = items[x-1]['created']
		print(email + ' ' + created[0:10])
		#=========================================
		# Compare the date created; if today - act
		#=========================================
		if today == created[0:10]:
			print('created today') 
			#hello =  items[x-1]['event_id']
			register_today.append(items[x-1]['order_id'])
			print(register_today)
	print('\n')
#=========================================================================
# For each attendee on that list, import their information into mail chimp
#
# This is a stupid second step where I just have to relook up the same information I had in the previous step
# I should just import them into mail chimp if they fit the requirements
#=========================================================================

for z in register_today:
	print(z)
	order = eventbrite.get('/orders/'+z+'/')
	print(order)
