from typing import Tuple

import tweepy
import arrow
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def the_time(offset: int) -> Tuple[str, str]:
    init = arrow.utcnow().shift(hours=offset/3600)
    time = init.format("HH:mm")
    date = init.format("dddd DD")
    return time, date


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


if __name__ == "__main__":
    listener = BotStreamer()
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['@RepliesWithTime'])
