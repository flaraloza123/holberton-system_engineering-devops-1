#!/usr/bin/python3

import requests

'''
top ten
'''


def top_ten(subreddit):
    ''' Returns top ten posts of a subreddit '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132i\
            Safari/537.36"
    headers = {"User-Agent": agent}
    r = requests.get(url, headers=headers).json()
    if r.get('error') == 404:
        print('None')
        return
    _list = r.get('data').get('children')
    for i, post in enumerate(_list[:10], 1):
        print(post.get('data').get('title', None))
