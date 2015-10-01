#!/Anaconda/python
from password import *
import twitter
import time
api = twitter.Api(consumer_key=ckey,
                      consumer_secret=csecret,
                      access_token_key=atoken,
                      access_token_secret=asecret)
#print api.VerifyCredentials()
#user = input("What twitter user do you want to look up?")					  
statuses = api.GetUserTimeline(screen_name="RealHughJackman")
#print [s.text for s in statuses]
#print [dir(s) for s in statuses]					  
print [s.retweet_count for s in statuses]
#Retweeted_status and FavoriteCount
#print [s.retweeted_status for s in statuses]
#ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
print [time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(s.created_at,'%a %b %d %H:%M:%S +0000 %Y')) for s in statuses]