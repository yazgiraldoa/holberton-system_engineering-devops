#!/usr/bin/python3
"""
Python ecursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the
given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], af=''):
    """Recursive function that queries Reddit API"""
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, af)
    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code == 404:
        return None

    json = r.json()
    if r.status_code == 200:
        for element in json['data']['children']:
            hot_list.append(element['data']['title'])
    af = json['data']['after']

    if af is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, af)
