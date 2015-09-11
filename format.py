#!/usr/bin/python3

import sys
from collections import OrderedDict
from string import punctuation


def clean_string(s):
    for c in punctuation:
        s = s.replace(c, " ")
    return s


def read_file(f):
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
        for w in l.split():
            if w.isalpha():
                dic[w] = 0
                dic.move_to_end(w)
        return dic


def format_data(f_out, lines, dic):
    with open(f_out, "w") as fout:
        for l in lines:
            l = l.split("\t")
            if len(l) == 1:
                continue
            grade = l[0]
            l = l[1:][0]
            fout.write("+1 " if grade[0] == "+" else "-1 ")
            l = clean_string(l)
            for w in l.split():
                if w.isalpha():
                    dic[w] += 1
            i = 1
            for key, value in dic.items():
                if(value != 0):
                    fout.write(str(i) + ":" + str(value) +
                               (" " if i != len(dic) else "\n"))
                else:
                    if i == len(dic):
                        fout.write("\n")
                i += 1
            clean_dic(dic)
            i = 1


def clean_dic(dic):
    for key in dic.keys():
        dic[key] = 0


def write_dic(f_dict):
    with open(f_dict, "w+") as fdict:
        for key in dic.keys():
            fdict.write(key + "\n")


def read_dic(f_dict):
    dic = OrderedDict()
    with open(f_dict, 'r') as f:
        for line in f.readlines():
            w = line.replace("\n", "")
            if w.isalpha():
                dic[w] = 0
                dic.move_to_end(w)
    return dic


if __name__ == "__main__":
    script, f_in, f_out = sys.argv
    dic = OrderedDict()
    lines = read_file(f_in)
    dic = build_dic(lines)
    write_dic("train.dict")
    print("Building vectors")
    format_data(f_out, lines, dic)
