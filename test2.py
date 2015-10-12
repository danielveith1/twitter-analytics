#!/Anaconda/python
from password import *
import twitter
import time
from datetime import date
import datetime 
import math
import random
import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo_ochl
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime
import types
import numpy

# authenticates the twitter app	
api = twitter.Api(consumer_key=ckey,
                      consumer_secret=csecret,
                      access_token_key=atoken,
                      access_token_secret=asecret)
#verifyCredentials only necessary to verify authentication
#print api.VerifyCredentials()
user = "RealHughJackman"
# obtaining timeline from a specific user					  
statuses = api.GetUserTimeline(screen_name=user)
# used dir(s) to find all the attributes of statuses that is retrived from the timeline
#print [dir(s) for s in statuses]					  
print "The Tweets of " + user + " and the retweets they received.\n"
for s in statuses:
	print dir(s)
	#print("On " + time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(s.created_at,'%a %b %d %H:%M:%S +0000 %Y')) + " the tweet received " + str(s.retweet_count) +" retweets.")
#FavoriteCount is another attribute that would be useful to analyze

#ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
#print [time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(s.created_at,'%a %b %d %H:%M:%S +0000 %Y')) for s in statuses]


'''
    for s in statuses:
		x = time.strftime('%Y-%m-%d', time.strptime(s.created_at,'%a %b %d +0000 %Y'))
		y = s.retweet_count

date1 = datetime.date(2015, 1, 1)
date2 = datetime.date(2015, 12, 12)

years = YearLocator()   # every year
months = MonthLocator()  # every month
yearsFmt = DateFormatter('%Y')




dates = [time.strptime(s.created_at,'%a %b %d %H:%M:%S +0000 %Y') for s in statuses]
opens = [s.retweet_count for s in statuses]

fig, ax = plt.subplots()
ax.plot_date(dates, opens, '-')

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax.autoscale_view()

# format the coords message box
def price(x): return '$%1.2f'%x
ax.fmt_xdata = DateFormatter('%Y-%m-%d')
ax.fmt_ydata = price
ax.grid(True)

fig.autofmt_xdate()
plt.show()
'''