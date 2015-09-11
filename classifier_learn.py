#!/usr/bin/python3

from textblob.classifiers import NaiveBayesClassifier
import pickle
import sys

if __name__ == "__main__":
    script, train, pick_out = sys.argv

    with open(train, 'r') as ftrain:
        cl = NaiveBayesClassifier(ftrain, format='csv')
        with open(pick_out, "wb") as p:
            pickle.dump(pickle.dumps(cl), p)
