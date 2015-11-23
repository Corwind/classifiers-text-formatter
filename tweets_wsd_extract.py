#!/usr/bin/python3

"""
wsdextract.py

Usage:
    wsdextract.py (-i|--input) <file_in> (-o|--output) <file_out>
    [-k|--keep-punct]

Options:
    -h --help           display help message
    -i --input          input file name
    -o --output         output file name
    -k --keep-punct     keep punctuation in results
"""

from pprint import pprint as print

NO_PUNCT = True

def extract_crf(fin, fout):
    lines = []
    temp = []
    chunks = {}
    linechunks = []
    with open(fin, 'r') as f:
        i = 0
        for line in f.readlines():
            if line.startswith('+++++++++++++'):
                lines.append(temp)
                if not i in chunks.keys():
                    chunks[i] = linechunks
                else:
                    chunks[i].append(linechunks)
                linechunks = []
                temp = []
                i += 1
                continue
            if line.startswith('-------------'):
                continue
            l = []
            line = line.split('\t')
            reverse_line = line[::-1]
            if int(reverse_line[0]) - int(reverse_line[1]) > 1:
                linechunks.append(line)
                continue
            s = line[2]
            print(s)
            s = s.replace(' ', '_')
            print(s)
            l.append(s)
            l.append(line[1])
            temp.append(l)
    for i in range(len(lines)):
        if not i in chunks.keys():
            continue
        line = lines[i]
        for ls in chunks[i]:
            b = int(ls[::-1][1])
            e = int(ls[::-1][0])
            if ls[1].startswith('*verb'):
                suffix = '-VP'
            else:
                suffix = '-NP'
            for j in range(b, e):
                if j == b:
                    if len(line[j]) < 3:
                        line[j].append('B' + suffix)
                    continue
                if j == e - 1:
                    if len(line[j]) < 3:
                        line[j].append('O' + suffix)
                    continue
                if len(line[j]) < 3:
                    line[j].append('I' + suffix)
    for line in lines:
        for l in line:
            if len(l) < 3:
                if l[1].startswith('verb'):
                    l.append('B-VP')
                else:
                    l.append('B-NP')
    finals = []
    for line in lines:
        if NO_PUNCT:
            line = [l for l in line if l[1] != 'punct']
        finals.append(line)
    lines = finals
    with open(fout, 'w') as f:
        for l in lines:
            for line in l:
                f.write(' '.join(line) + '\n')
            f.write('\n')

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    inp = arguments['<file_in>']
    outp = arguments['<file_out>']
    NO_PUNCT = not arguments['--keep-punct']
    extract_crf(inp, outp)
