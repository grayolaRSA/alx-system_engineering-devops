#!/usr/bin/python3
"""
Module for the subreddit API queries
"""
import requests
import sys


def top_ten(subreddit):
    """ Subreddit top ten titles reddit API method """

    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = (f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10")
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    dc = res.json()
    hotPosts = dc['data']['children']
    if len(hotPosts) == 0:
        print(None)
    else:
        for post in hotPosts:
            print(post['data']['title'])


if __name__ == "__main__":
    subreddit = sys.argv[1]
