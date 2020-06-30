#!/usr/bin/python3

'''
count words
'''

from collections import Counter, defaultdict
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
    try:
        r = requests.get(url, headers=headers, allow_redirects=False).json()
        titles = r.get('data').get('children')
        for t in titles:
            split_title = t.get('data').get('title').lower().split(' ')
            count(res, word_list, split_title)
        after = r.get('data').get('after')
        if not after:
            return print_sorted_dict(res)
        return count_words(subreddit, word_list, res, after)
    except Exception:
        return


def count(res, word_list, title):
    ''' count words in a sentence from a given list'''
    word_list = [x for x in word_list]
    for word in word_list:
        if word.lower() in title:
            res[word] += 1


def print_sorted_dict(res):
    ''' print sorted dictionary '''
    for k, v in sorted(res.items(), key=lambda x: x[1], reverse=True):
        print('{}: {}'.format(k, v))
