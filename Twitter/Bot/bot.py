import tweepy as twitter
import time
import re
from decouple import config

API_KEY = config('API_KEY')
API_SECRET_KEY = config('API_SECRET_KEY')
BEARER_TOKEN = config('BEARER_TOKEN')
ACCESS_TOKEN  = config('ACCESS_TOKEN')
ACCESS_SECRET = config('ACCESS_SECRET')

class TwitterBot:
    def __init__(self):
        self.api = TwitterBot.authenticate()
    def authenticate(self):
        auth = twitter.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = twitter.API(auth)
        return api
    def retweet_bot(self, hashtag, delay):
        while True:
            for tweet in twitter.Cursor(self.api.search, q=hashtag, rpp=100).items(40):
                try:
                    if len(re.findall(r"(Day \d+)|(#Day \d+)|(day \d+)|(#day \d+)|(#Python_everywhere)|(@LebotPython)|(D\d+)|(#Day\d+)", str(dict(tweet._json)["text"]))):
                        print(f"\n{time.strftime('%I:%M:%S %p')}\n")
                        print(f"{time.strftime('%a %d,%b %Y')}\n")
                        tweet_id = dict(tweet._json)["id"]
                        tweet_tweet = dict(tweet._json)["text"]
                        # name = dict(tweet._json)["user"]    #['screen_name']
                        print("id: " + str(tweet_id))
                        print("tweet: "+ str(tweet_tweet))
                        # print(dir(tweet.user.follow))
                        # print(f"Posted by: " +str(name))
                        self.api.retweet(tweet_id)
                    
                except twitter.TweepError as err:
                    print(err.reason)               

            time.sleep(delay)


if __name__ == '__main__':
    bot = TwitterBot()
    bot.retweet_bot("#100DaysOfCode", 60)

