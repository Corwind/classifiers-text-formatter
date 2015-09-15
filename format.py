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
    lines = []
    with open(f_in, "r") as f:
        lines = f.readlines()
    return lines


def build_dic(lines):
    print("Building dictionnary")
    for line in lines:
        l = line.split("\t")
        if len(l) == 1:
            lines.remove(line)
            continue
        l = l[1]
        l = clean_string(l)
        for w in bigrams(l):
            dic[w] = 0
            dic.move_to_end(w)
    return dic


def format_data(f_out, lines, dic):
    grades = []
    clean_lines = []
    for l in lines:
        l = l.split("\t")
        if len(l) == 1:
            continue
        grade = l[0]
        grades.append("+1 " if grade[0] == "+" else "-1 ")
        l = l[1:][0]
        l = clean_string(l)
        clean_lines.append(l)
    idf = compute_idf(clean_lines, dic)
    with open(f_out, "w") as fout:
        for j in range(len(clean_lines)):
            if (j % 100) == 0:
                print(str(j) + "\n")
            for word in bigrams(clean_lines[j]):
                tf = compute_tf(word, clean_lines[j])
                try:
                    dic[word] = tf * idf[word]
                except:
                    print("FAIL")
            fout.write(grades[j])
            i = 1
            for key, value in dic.items():
                if(value != 0):
                    fout.write(str(i) + ":" + str(value) +
                               (" " if i != len(dic) else "\n"))
                else:
                    if i == len(dic):
                        fout.write("\n")
                i += 1
            clean_dic(dic, clean_lines[j])
            i = 1


def clean_dic(dic, line):
    for word in line.split():
        try:
            dic[word] = 0
        except:
            pass


def write_dic(f_dict):
    with open(f_dict, "w+") as fdict:
        for key in dic.keys():
            fdict.write(key)
            fdict.write("\n")


def read_dic(f_dict):
    dic = OrderedDict()
    with open(f_dict, 'r') as f:
        for line in f.readlines():
            w = line.replace("\n", "")
            if w.isalpha():
                dic[w] = 0
                dic.move_to_end(w)
    return dic


def compute_tf(word, line):
    i = 0
    words = bigrams(line)
    for w in words:
        if w == word:
            i += 1
    tf = i / len(words)
    return tf


def compute_idf(lines, dic):
    idf = OrderedDict()
    for key in dic.keys():
        i = 0
        for line in lines:
            if key in bigrams(line, compute_idf):
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

if __name__ == "__main__":
    script, f_in, f_out = sys.argv
    dic = OrderedDict()
    lines = read_file(f_in)
    dic = build_dic(lines)
    write_dic("train.dict")
    print("Building vectors")
    format_data(f_out, lines, dic)
