#!/usr/bin/python3

import requests

'''
recurse
'''


def recurse(subreddit, hot_list=[], after=None):
    ''' Returns top ten posts of a subreddit '''
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132i\
            Safari/537.36"
    headers = {"User-Agent": agent}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    r = requests.get(url, headers=headers).json()
    if r.get('error') == 404:
        return None
    _list = r.get('data').get('children')
    for li in _list:
        hot_list.append(li.get('data').get('title'))
    after = r.get('data').get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
