'''Put this program on a server

   This program will retweet - wipro digital and designit every 2 hours.

   It only tweets things that they post originally - it will not retweet their retweets

   You can run it continuously on a server ...

   Or you can turn it into a cron job that runs once every 2 hours

'''

import tweepy
from time import sleep
from datetime import datetime, timedelta
import re

# is retweet regular expression

isretweet = re.compile(r'^RT\s')
ms = re.compile(r'\+\d+\s')

# @rossegates
'''
api_key = "edKVh0eoHHAr1fBZVOn3jUNrT"
api_secret = "mphroKgqsx5qsonQWcwU81xfQBoeEEVSV6MTaEtSa1iLG0mn9x"
ac_token = "799091833540374528-2Zav1SJ0Y6c2Rz5kAJs0YpuytZhOZGN"
ac_secret = "twk1vK6pzA441LJlw4PjODuyxAGQ7bncuZhrOF4yjPuEx"
'''

# @cooper
api_key = "p0B41OOn03PDK4VL8CS8HJO6Q"
api_secret = "VDtpdPHVIeLgkOSwYPKyIP3EhbJmQQm5tqplxVgA3Pf9Aux3hU"
ac_token = "17223242-wb7vfckd6DjoOUMkIwwPajRT7xT2AsQ135yd4qU6J"
ac_secret = "oRPEqE9916DwXXL1iXdvz8c5y1xc7lfcJ1d4Kh8zCWgBp"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(ac_token, ac_secret)

api = tweepy.API(auth)

now = datetime.now()
three_hours = now

accounts_to_retweet = ['wiprodigital','designit']

while True:
    for tw_account in accounts_to_retweet:
        for status in api.user_timeline(tw_account):
            # is an original tweet from this account
            if not isretweet.search(status.text):
                # was tweeted in the last 3 hours
                unformatted = status.created_at
                epoch = datetime.utcfromtimestamp(0)
                now_ms = (now - epoch).total_seconds()
                print(now_ms)
                tweet_ms = (unformatted - epoch).total_seconds()
                print(tweet_ms)
                tw_difference = now_ms - (tweet_ms-23400-1565)
                # retweet everything that has happened in the last 2 hours
                if (tw_difference) < 7200:
                    status.retweet()
                    print(status.text)
    sleep(7200)



