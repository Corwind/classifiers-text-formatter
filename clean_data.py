#!/usr/bin/python3

import re
import sys
from nltk.corpus import stopwords
from nltk.stem.snowball import PorterStemmer as Stemmer
from format import clean_string as cls


def clean_occurences(lines):
    dic = {}
    for line in lines:
        for word in line.split():
            if word.isalpha():
                try:
                    dic[word] += 1
                except:
                    dic[word] = 1
    to_rm = []
    for key, value in dic.items():
        if value < 2:
            to_rm.append(key)
    pattern = re.compile(r'\b(' + r'|'.join(to_rm) + r')\b\s*')
    for i in range(len(lines)):
        if not (len(to_rm) == 0):
            lines[i] = pattern.sub('', lines[i])
    return lines

if __name__ == "__main__":
    not_stopw = ["no", "nor", "not", "over", "under", "again", "further",
            "but", "against", "too", "very"]
    stopw = stopwords.words('english')
    for x in not_stopw:
        stopw.remove(x)
    stemmer = Stemmer()
    pattern = re.compile(r'\b(' + r'|'.join(stopw) + r')\b\s*')
    script, fin, fout = sys.argv
    with open(fin, 'r') as f_in:
        lines = f_in.readlines()
        grades = []
        for i in range(len(lines)):
            line = lines[i].split("\t")
            grades.append(line[0])
            lines[i] = line[1].replace("\n", "")
            lines[i] = cls(lines[i])
        for i in range(len(lines)):
            lines[i] = lines[i].lower()
            lines[i] = pattern.sub('', lines[i])
            lines[i] = " ".join([stemmer.stem(w) for w in lines[i].split()])
        lines = clean_occurences(lines)
        with open(fout, 'w') as f_out:
            for i in range(len(lines)):
                f_out.write(grades[i] + "\t" + lines[i] + "\n")
