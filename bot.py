from typing import Tuple

import tweepy
import arrow
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class BotStreamer(tweepy.StreamListener):

    def on_status(self, status: any) -> None:
        print(status)
        username = status.user.screen_name
        status_id = status.id
        offset = status.user.utc_offset
        location = status.user.location

        time, date = the_time(offset)

        status = f"@{username}, the time is {time} on {date}"
        if location:
            status += f" in {location}"
        api.update_status(status=status, in_reply_to_status=status_id)


def the_time(offset: int) -> Tuple[str, str]:
    init = arrow.utcnow().shift(hours=offset/3600)
    time = init.format("HH:mm")
    date = init.format("dddd DD")
    return time, date


listener = BotStreamer()
stream = tweepy.Stream(auth, listener)
stream.filter(track=['@replieswithtime'])
