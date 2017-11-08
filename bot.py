import tweepy
import time
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class BotStreamer(tweepy.StreamListener):

    def on_status(self, status) -> None:
        print(status)
        username = status.user.screen_name
        status_id = status.id

        api.update_status(status=f"@{username} :: {the_time()}", in_reply_to_status=status_id)


def the_time() -> str:
    localtime = time.asctime(time.localtime(time.time()))
    return localtime


listener = BotStreamer()
stream = tweepy.Stream(auth, listener)
stream.filter(track=['@replieswithtime'])
