#!/usr/bin/python3

'''
count words
'''

from collections import Counter, defaultdict
import re
import requests


def count_words(subreddit, word_list, res=defaultdict(int), after=None):
    ''' count words in a subreddit '''
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132i\
            Safari/537.36"
    headers = {"User-Agent": agent}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    r = requests.get(url, headers=headers, allow_redirects=False).json()
    titles = r.get('data').get('children')
    for t in titles:
        c = Counter(t.get('data').get('title').lower().split(' '))
        for word in word_list:
            res[word] += c.get(word.lower(), 0)
    after = r.get('data').get('after')
    if after:
        return count_words(subreddit, word_list, res, after)
    for k, v in sorted(res.items(),
                       key=lambda x: (x[1], x[0]),
                       reverse=True):
        print('{}: {}'.format(k, v))
