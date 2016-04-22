#!/usr/bin/python3

import sys

if __name__ == "__main__":
    script, f1, f2 = sys.argv
    correct = 0
    lines1 = []
    with open(f1, 'r') as f:
        lines1 = f.readlines()
    lines2 = []
    with open(f2, 'r') as f:
        lines2 = f.readlines()
    total = len(lines1)
    for i in range(total):
        if (lines1[i][0] == lines2[i][0]) or (lines1[i][0] != '-' and
                lines2[i][0] == '+'):
            correct += 1
    print("{:.2%}".format(float(correct) / float(total)))
