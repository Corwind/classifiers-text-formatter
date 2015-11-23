#!/usr/bin/python3

"""
twitter_chunk_results.py

Usage:
    twitter_chunk_results.py -i <results>

Options:
    -h --help   print this help message
    -i          input file

"""

from pprint import pprint as print
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    inp = arguments['<results>']
    total = 0
    goods = 0
    with open(inp, 'r') as f:
        for line in f.readlines():
            line = line.split('\t')
            if len(line) < 4:
                continue
            total += 1
            if line[2] == line[3].replace('\n', ''):
                goods += 1
    print(float(goods) / float(total))
