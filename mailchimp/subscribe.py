
#03b2adc07d: Eleframes Newsletter (Subscribers: 11)
#215d1a3293: Entrepreneurial Supporters (Subscribers: 16)
#4a60ee669f: testAPI (Subscribers: 0)
#862c3ece17: Eleframes Newsletter (Subscribers: 300)
#b299388867: Eleframes Organizations (Subscribers: 1)




import mailchimp
API_KEY = '4a55a624d3aec306a7af411134eced91-us12'
LIST_ID = '4a60ee669f'

api = mailchimp.Mailchimp(API_KEY)
api.lists.subscribe(LIST_ID,{"email_address": "openspace@rossegates.com","status": "subscribed","merge_fields":{"FNAME": "Urist","LNAME":"McVankab"}})
