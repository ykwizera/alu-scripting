#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests
import praw

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    reddit = praw.Reddit(client_id='my_client_id',
                           client_secret='my_client_secret',
                           user_agent='my_user_agent')

    try:
        subreddit_data = reddit.subreddit(subreddit)
        subscribers = subreddit_data.subscribers
        return subscribers
    except praw.exceptions.NotFound:
        return 0
