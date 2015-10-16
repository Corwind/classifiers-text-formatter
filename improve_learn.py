#!/usr/bin/python3

import subprocess
import sys

OUTPUT_PREFIX = "/output_{}"
MODEL_PREFIX = "/model_{}"
TEST_PREFIX = "/test_{}"
TRAIN_PREFIX = "/train_{}"
STDOUT_CLASSIF_PREFIX = "/stdout_{}"
ERROR_FILE = open("errors", 'w')

def append_learn(train_file, output_train_file, test_file, result_file):
  with open(train_file, 'r') as tf:
    with open(output_train_file, 'w') as otf:
      with open(test_file, 'r') as tef:
        with open(result_file, 'r') as rf:
          train_lines = tf.readlines()
          for line in train_lines:
            otf.write(line)
          test_lines = tef.readlines()
          result_lines = rf.readlines()
          for i in range(len(test_lines)):
            if ((test_lines[i][0] == '-' and result_lines[i][0] == '-') or
                (test_lines[i][0] == '+' and result_lines[i][0] != '-')):
              otf.write(test_lines[i])
            else:
              ERROR_FILE.write(test_lines[i])

if __name__ == "__main__":
  script, d, b, e = sys.argv
  for i in range(int(b), int(e)+1):
    print(str(i))
    subprocess.call(["vw", "--ngram", "2", "--skips", "1", d + TRAIN_PREFIX.format(i-1), "-f",
      d + MODEL_PREFIX.format(i)])
    stdout_ = open(d + STDOUT_CLASSIF_PREFIX.format(i), "w")
    subprocess.call(["vw", "--ngram", "2", "--skips", "1", "-t", d + TEST_PREFIX.format(i), "-i",
        d + MODEL_PREFIX.format(i), "-p", d + OUTPUT_PREFIX.format(i)],
      stdout=stdout_)
    append_learn(d + TRAIN_PREFIX.format(i-1), d + TRAIN_PREFIX.format(i),
        d + TEST_PREFIX.format(i), d + OUTPUT_PREFIX.format(i))
  ERROR_FILE.close()
