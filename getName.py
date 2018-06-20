import time
from eventbrite import Eventbrite
#WORKS prints the objects inside the eventbrite file             print(dir())

eventbrite = Eventbrite('D6P5CGYEQMZQXPBSPJDG')
user = eventbrite.get_user()  # Not passing an argument returns yourself


# These all work
#print( user['id'])
#print(user['name'])
#print(user.pretty)

# Get my own User ID
my_id = eventbrite.get_user()['id']

# Get a raw list of events (includes pagination details)
#WORKS events = eventbrite.event_search(**{'user.id': my_id})
#WORKS print(eventbrite.get('/users/me'))
#WORKS print(eventbrite.get('/orders/622941455/'))
#Does Not Work - print(eventbrite.get('/orders/*/'))
# List the events in draft status
#print([x for x in events['events'] if x['status'] == 'live'])
#[y for x in events['events'] if x['status'] == 'live']

#for x in events['events']:
#	if x['status'] == 'live':
#WORKS		print(x)
#		print(x.get('name'))
#		y = x.get('end')
#		print(y.get('local'))
#print(y.end)
#print(x.pretty)


#print(eventbrite.get('/events/34072776592/attendees/?expand=profile'))

#=====================
# Get the current date
#=====================
today = time.strftime("%Y-%m-%d")
print (time.strftime("%Y-%m-%d"))


#=============================
# Get all eventbrite attendees
#=============================

attend = eventbrite.get('/events/34072776592/attendees/')
#page = attend.get('pagination')
#count = page.get('object_count')
#items = attend.get('attendees')

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
  	
	print('\n')

#print(count)
