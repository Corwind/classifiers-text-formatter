#!/usr/bin/zsh

N=$@

for ((i=1; i < $N; i++))
do
  ./src/format_test.py ./tests/data_test_"$i"_clean ./tests/test_"$i"_clean;
  scp ./tests/test_"$i"_clean ssaling02:/home/dore/projects/
done
