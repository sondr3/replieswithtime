"""A dumb twitter bot that replies with the time if asked."""
import random
from typing import Dict

import pendulum
from TwitterAPI import TwitterAPI

from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET


def authenticate() -> TwitterAPI:
    """Authenticate the bot with Twitter and return the API and handle."""
    return TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)


def greeting() -> str:
    """Return a nice greeting for our replier."""
    greetings = ['Have a nice day!', 'Enjoy!', 'Have a great day!',
                 'Have a good one!', 'Take care!', 'Go forth and prosper']

    return random.choice(greetings)


def reply(tweet: Dict, api: TwitterAPI) -> None:
    """Reply to the user who mentioned the bot."""
    username = tweet['user']['screen_name']
    status_id = tweet['id']

    time = pendulum.now(tz="UTC").format("HH:mm")
    date = pendulum.now(tz="UTC").format("dddd, MMMM Do")

    status = f"@{username}, GMT time is {time}, {date}. "
    status += f"{greeting()}"
    api.request('statuses/update', {'status': status, 'in_reply_to_status_id': status_id})
    print(status)
    print("[Posted new status!]")


if __name__ == "__main__":
    print("[Bot starting up...]")
    API = authenticate()
    while True:
        stream = API.request('statuses/filter', {'track': '@RepliesWithTime'})
        for t in stream.get_iterator():
            print(t)
            reply(t, API)
