#!/usr/bin/python3

"""
twitter_chunk_results.py

Usage:
    twitter_chunk_results.py -i <results>

Options:
    -h --help   print this help message
    -i          input file

"""

import sys
from pprint import pprint
from docopt import docopt


def results(lines):
    total = 0
    goods = 0
    for line in lines:
        line = line.split('\t')
        if len(line) < 4:
            continue
        total += 1
        if line[-2] == line[-1].replace('\n', ''):
            goods += 1
    print("Accuracy : {}".format((float(goods) / float(total)) * 100), file=sys.stderr)

def show_chunks(lines):
    phrase = []
    chunks = []
    ch = []
    for line in lines:
        line = line.strip().split('\t')
        if len(line) > 1:
            phrase.append(line[0])
            if line[-1].startswith('B'):
                if len(ch) != 0:
                    chunks.append(ch)
                    ch = []
            ch.append(line[0])
        else:
            print(' '.join(phrase))
            pprint(chunks)
            print()
            phrase = []
            chunks = []




if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    inp = arguments['<results>']
    with open(inp, 'r') as f:
        lines = f.readlines()
    show_chunks(lines)
    results(lines)
