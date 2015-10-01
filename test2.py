#!/Anaconda/python
from password import *
import twitter
import time
import math
import matplotlib 
import matplotlib.pyplot
import types
import numpy
import bisect
def show_plot(arg1, arg2=None):

    def real_decorator(f):
        def wrapper(*args, **kwargs):
            matplotlib.pyplot.figure(figsize=(arg1, arg2))
            result = f(*args, **kwargs)
            matplotlib.pyplot.show()
            return result
        return wrapper

    if type(arg1) == types.FunctionType:
        f = arg1
        arg1, arg2 = 10, 5
        return real_decorator(f)
    return real_decorator
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


@show_plot
def simple():
    x_data = numpy.linspace(0., 100., 1000)

    for s in statuses:
		x = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(s.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
		y = s.retweet_count
		matplotlib.pyplot.scatter(x,y)

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Date')
    axes.set_ylabel('Number of tweets')

simple()