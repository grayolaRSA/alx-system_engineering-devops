#!/usr/bin/python3
"""api module to get number of reddit subscribers for a subreddit"""
import praw
import prawcore.exceptions
import sys


def number_of_subscribers(subreddit):
    """method to retrieve the number of reddit subcribers"""

    if not subreddit:
        return 0

    # Create a Reddit instance
    reddit = praw.Reddit(
        client_id='F3jxoROf0m2Phw3to2QuLA',
        client_secret='89vvf_RLXwjzISEyUslqv_O2u8303w',
        user_agent='YOUR_USER_AGENT'
    )
    subreddit_name = subreddit
    try:
        # Get the subreddit object
        subreddit = reddit.subreddit(subreddit_name)

        # Get the number of subscribers
        subscribers_count = subreddit.subscribers

        return subscribers_count

    except prawcore.exceptions.NotFound:
        return 0


if __name__ == "__main__":
    subreddit_name = sys.argv[1]
    subscribers = number_of_subscribers(subreddit_name)
#   print(f"The '{subreddit_name}' subreddit has {subscribers} subscribers.")
