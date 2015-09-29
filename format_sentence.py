#!/usr/bin/python3

import sys
from math import log10
from collections import OrderedDict
from string import punctuation
from string import digits


def clean_string(s):
    for c in punctuation:
        s = s.replace(c, " ")
    for c in digits:
        s = s.replace(c, "")
    return s


def read_file(f_in):
    with open(f_in, "r") as f:
        line = f.readline()
    return line


def build_dic(lines):
    for line in lines:
        l = line.split("\t")
        if len(l) == 1:
            lines.remove(line)
            continue
        l = l[1]
        l = clean_string(l)
        words = bigrams(l) + l.split()
        for w in words:
            dic[w] = 0
            dic.move_to_end(w)
    return dic


def format_data(f_out, line, dic, w = False):
    clean_line = clean_string(line)
    words = bigrams(clean_line) + clean_line.split()
    with open(f_out, "w") as fout:
        for word in words:
            try:
                dic[word] += 1
            except:
                pass
        i = 1
        fout.write("0 ")
        for key, value in dic.items():
            if(value != 0):
                fout.write(str(i) + ":" + str(value) +
                            (" " if i != len(dic) else "\n"))
            else:
                if i == len(dic):
                    fout.write("\n")
            i += 1
        dic = clean_all_dic(dic)
        i = 1

def clean_all_dic(dic):
    for key in dic.keys():
        dic[key] = 0
    return dic

def clean_dic(dic, line):
    for word in line.split():
        try:
            dic[word] = 0
        except:
            pass
    return dic


def write_dic(f_dict, dic):
    with open(f_dict, "w+") as fdict:
        for key in dic.keys():
            fdict.write(key)
            fdict.write("\n")


def read_dic(f_dict):
    dic = OrderedDict()
    with open(f_dict, 'r') as f:
        for line in f.readlines():
            w = line.replace("\n", "")
            if map(str.isalpha, w.split()):
                dic[w] = 0
                dic.move_to_end(w)
    return dic


def compute_tf(word, line):
    i = 0
    words = bigrams(line) + line.split()
    for w in words:
        if w == word:
            i += 1
    tf = i / len(words)
    return tf


def compute_idf(lines, dic, bigram_arrray):
    idf = OrderedDict()
    for key in dic.keys():
        i = 0
        for j in range(len(lines)):
            words = bigram_arrray[j] + lines[j].split()
            if key in words:
                i += 1
        if i == 0:
            continue
        idf[key] = log10(float(len(lines)) / float(i))
    return idf

def bigrams(line, debug=None):
    if debug:
        print(str(debug))
    ls = line.split()
    z = zip(*[ls[i:] for i in [0, 1]])
    z = [bigram[0] + " " + bigram[1] for bigram in z]
    return z

def corpus_bigrams(corpus):
    b = []
    for line in corpus:
        b.append(bigrams(line, corpus_bigrams))
    return b

if __name__ == "__main__":
    script, f_in, f_out = sys.argv
    dic = OrderedDict()
    lines = read_file(f_in)
    dic = read_dic("train.dict_98")
    format_data(f_out, lines, dic)
