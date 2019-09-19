#!/usr/bin/python3

import requests

'''
count
'''


def count_words(subreddit, word_list, _dict={}, after=None):
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
        _list = r.get('data').get('children')
        for li in _list:
            title = li.get('data').get('title').lower().split(' ')
            _dict = count(_dict, word_list, title)
        after = r.get('data').get('after')
        if after is None:
            print_sorted_dict(_dict)
            return
        return count_words(subreddit, word_list, _dict, after)
    except Exception:
        return None


def count(_dict, word_list, sentence):
    ''' count words in a sentence from a given list'''
    for s in sentence:
        if s in set([x.lower() for x in word_list]):
            if _dict.get(s):
                _dict[s] += 1
            else:
                _dict[s] = 1
    return _dict


def print_sorted_dict(_dict):
    ''' print sorted dictionary '''
    for k, v in sorted(_dict.items(), key=lambda x: x[1], reverse=True):
        print('{}: {}'.format(k, v))
