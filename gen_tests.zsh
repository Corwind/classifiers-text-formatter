#!/usr/bin/zsh

N=$1

for ((i=1; i < $N; i++))
do
  ./src/format.py -d learn.dict -i ./tests/data_test_"$i"_clean -o ./tests/test_"$i"_clean -f format_test --use-idf;
  scp ./tests/test_"$i"_clean ssaling02:/home/dore/projects/
done
