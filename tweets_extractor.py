#!/usr/bin/python3

"""
tweets_extractor.py

usage:
    tweets_extractor.py (-d|--dump) <dump> -o <output>

Options:
    -h --help       Print this message
    -d --dump       Specify the dump file
    -o --output     Specify the output file
"""

import re
from docopt import docopt

def retrieve_tweets(dump):
    with open(dump, 'r') as f:
        tweets = [l.split('\t')[8] for l in f.readlines()]
    return tweets

def write_tweets(tweets, output):
    with open(output, 'w') as f:
        for i in range(len(tweets)):
            tweets[i] = re.sub("_[A-Z]{5}_", "", tweets[i])
        f.write('\n'.join(tweets))

if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.1')
    dump = arguments['<dump>']
    output = arguments['<output>']
    write_tweets(retrieve_tweets(dump), output)
