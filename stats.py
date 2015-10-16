#!/usr/bin/python3

import sys

if __name__ == "__main__":
    script, d = sys.argv
    l = [0] * 100
    with open(d + "/percents", 'r') as f:
        for line in f.readlines():
            l[int(line[0:2])] += 1
        for i in range(100):
            if (l[i] != 0):
                print("{0}%: {1}".format(i, l[i]))
