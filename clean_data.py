#!/usr/bin/python3

import re
import sys
from nltk.corpus import stopwords
from nltk.stem.snowball import PorterStemmer as Stemmer


if __name__ == "__main__":
    stopw = stopwords.words('english')
    stemmer = Stemmer()
    pattern = re.compile(r'\b(' + r'|'.join(stopw) + r')\b\s*')
    script, fin, fout = sys.argv
    with open(fin, 'r') as f_in:
        lines = f_in.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].lower()
            lines[i] = pattern.sub('', lines[i])
            lines[i] = " ".join([stemmer.stem(w) for w in lines[i].split()])
        with open(fout, 'w') as f_out:
            for line in lines:
                f_out.write(line.replace(" ", "\t", 1) + "\n")
