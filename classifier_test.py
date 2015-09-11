#!/usr/bin/python3

"""
classifier_test.py

Usage:
    classifier_test.py -p <pickle> (-f <test> | -c <sentence>) [--accuracy]

Options:
    -h --help       Print this message
    -v --version    Print the version
    -p              The file containing the pickle dump of the trained classifier
    -f              The file used to test the trained classifier
    -c              The sentence to classify
    --accuracy      Display the accuracy of the classifier

"""


from textblob.classifiers import NaiveBayesClassifier
import pickle
from docopt import docopt

if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.1')
    print(arguments)
    pick_in = arguments['<pickle>']
    test = arguments['<test>']
    to_class = arguments['-c']
    sentence = arguments['<sentence>']
    acc = arguments['--accuracy']

    with open(pick_in, "rb") as p:
        cl = pickle.loads(pickle.load(p, encoding="ASCII"))
        test_set = []
        if to_class:
            print(cl.classify(sentence))
        else:
            with open("result", "w") as r:
                with open(test, 'r') as t:
                    for line in t.readlines():
                        line_split = line.split(",")
                        test_set.append((line_split[0], line_split[1].replace("\n", "")))
                        if arguments['-f']:
                            r.write(line_split[0] + "," + cl.classify(line_split[0]) + "\n")
        if acc:
            print(cl.accuracy(test_set))
