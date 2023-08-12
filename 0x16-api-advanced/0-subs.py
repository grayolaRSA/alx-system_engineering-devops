#!/usr/bin/python3
"""api module to get number of reddit subscribers for a subreddit"""
import praw
import sys


def number_of_subscribers(subreddit):
    """method to retrieve the number of reddit subcribers"""

    # Create a Reddit instance
    reddit = praw.Reddit(
        client_id='F3jxoROf0m2Phw3to2QuLA',
        client_secret='89vvf_RLXwjzISEyUslqv_O2u8303w',
        user_agent='YOUR_USER_AGENT'
    )
    subreddit = sys.argv[1]
    subreddit_name = subreddit

    # Get the subreddit object
    subreddit = reddit.subreddit(subreddit_name)

    # Get the number of subscribers
    subscribers_count = subreddit.subscribers

    return subscribers_count


if __name__ == "__main__":
    subreddit_name = sys.argv[1]
    subscribers = number_of_subscribers(subreddit_name)
    print(f"The '{subreddit_name}' subreddit has {subscribers} subscribers.")
