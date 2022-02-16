#!/usr/bin/python3
"""
Python function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Function that queries Reddit API"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    r = requests.get(url, headers=headers, allow_redirects=False)
    json = r.json()
    if r.status_code == 200:
        for element in json['data']['children']:
            print(element['data']['title'])
    elif r.status_code == 404:
        print(None)
