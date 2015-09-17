#!/usr/bin/zsh


FILES=("aaaia" "aaaic" "aaaie" "aaaig" "aaaij" "aaail" "aaain" "aaaip" "aaair" "aaait" "aaaiv" "aaaix" "aaaiz" "aaaib" "aaaid" "aaaif" "aaaih" "aaaik" "aaaim" "aaaio" "aaaiq" "aaais" "aaaiu" "aaaiw" "aaaiy")

i=1

for file in $FILES
do
  ./src/clean_data.py data/$file ./tests/data_test_"$i"_clean
  i=$(($i + 1))
done
