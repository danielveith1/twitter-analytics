#!/Anaconda/python
from password import *
import twitter
api = twitter.Api(consumer_key=ckey,
                      consumer_secret=csecret,
                      access_token_key=atoken,
                      access_token_secret=asecret)
print api.VerifyCredentials()
					  
statuses = api.GetUserTimeline(screen_name=user)
#print [s.text for s in statuses]					  