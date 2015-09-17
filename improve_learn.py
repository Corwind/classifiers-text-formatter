#!/usr/bin/python3

import subprocess

OUTPUT_PREFIX = "results/output_{}"
MODEL_PREFIX = "results/model_{}"
TEST_PREFIX = "results/test_{}"
TEST_SUFFIX = "_clean"
TRAIN_PREFIX = "results/train_{}"
STDOUT_CLASSIF_PREFIX = "results/stdout_{}"

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

if __name__ == "__main__":
  for i in range(1, 26):
    print(str(i))
    subprocess.call(["svm_learn", TRAIN_PREFIX.format(i-1),
      MODEL_PREFIX.format(i)])
    stdout_ = open(STDOUT_CLASSIF_PREFIX.format(i), "w")
    subprocess.call(["svm_classify", TEST_PREFIX.format(i) + TEST_SUFFIX,
      MODEL_PREFIX.format(i), OUTPUT_PREFIX.format(i)],
      stdout=stdout_)
    append_learn(TRAIN_PREFIX.format(i-1), TRAIN_PREFIX.format(i),
        TEST_PREFIX.format(i) + TEST_SUFFIX, OUTPUT_PREFIX.format(i))
