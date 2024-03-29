#!/usr/bin/python3
"""
Module for the reddit API queries
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Reddit API method """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = (f"https://www.reddit.com/r/{subreddit}/about.json")
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return res.json()['data']['subscribers']
