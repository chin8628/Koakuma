from twitter import *
from key import *
from setting import *
import pprint

class Api:

    twitter = None

    def __init__(self):
        self.twitter = Twitter(auth=OAuth(TOKEN, TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

    def get_user_timeline(self):
        response = self.twitter.statuses.user_timeline()
        return response
