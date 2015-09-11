#!/usr/bin/python3

import sys
from string import punctuation as punk

if __name__ == '__main__':
    script, fin, fout = sys.argv
    with open(fin, 'r') as f_in:
        with open(fout, 'w') as f_out:
            for line in f_in.readlines():
                line = line.replace("\n", "")
                line_split = line.split("\t")
                if len(line_split) == 1:
                    continue
                for c in punk:
                    line_split[1] = line_split[1].replace(c, "")
                print(line_split[0])
                f_out.write(line_split[1] + "," +
                           ("pos" if line_split[0][0] == "+" else "neg") + "\n")
