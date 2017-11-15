"""A dumb twitter bot that replies with the time if asked."""
from typing import Tuple, Any
import random

from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

import tweepy
from tweepy import OAuthHandler
import arrow


def authenticate() -> Tuple[tweepy.API, OAuthHandler]:
    """Authenticate the bot with Twitter and return the API and handle."""
    twitter_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    return tweepy.API(twitter_auth), twitter_auth


def the_time(offset: int) -> Tuple[str, str]:
    """Find the time at the users location and returns the time and date."""
    init = arrow.utcnow().shift(hours=offset/3600)
    time = init.format("HH:mm")
    date = init.format("dddd, MMMM Do")
    return time, date


def greeting() -> str:
    """Return a nice greeting for our replier."""
    greetings = ['Have a nice day!', 'Enjoy!', 'Have a great day!',
                 'Have a good one!', 'Take care!', 'Go forth and prosper']

    return random.choice(greetings)


class BotStreamer(tweepy.StreamListener):
    """Listen on Twitter and posts a new tweet if bot is mentioned."""

    @staticmethod
    def on_status(status: Any) -> None:
        """Reply to the user who mentioned the bot."""
        twitter = authenticate()[0]
        print(status)
        username = status.user.screen_name
        status_id = status.id
        offset = status.user.utc_offset
        location = status.user.location

        time, date = the_time(offset)

        status = f"@{username}, the time is {time} on {date}"
        if location:
            status += f" in {location}."
        else:
            status += "."
        status += f"{greeting()}"
        twitter.update_status(status=status, in_reply_to_status=status_id)
        print(status)
        print("[Posted new status!]")


if __name__ == "__main__":
    API, AUTH = authenticate()
    print("[Bot starting up...]")
    LISTENER = BotStreamer()
    STREAM = tweepy.Stream(AUTH, LISTENER)
    STREAM.filter(track=['@RepliesWithTime'])
