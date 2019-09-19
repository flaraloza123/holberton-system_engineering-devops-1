#!/usr/bin/python3

import requests

'''
number_of_subscribers
'''


def number_of_subscribers(subreddit):
    ''' Returns number of subscribers '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132i\
            Safari/537.36"
    headers = {"User-Agent": agent}
    r = requests.get(url, headers=headers).json().get('data')
    if r:
        return r.get('subscribers')
    return 0
