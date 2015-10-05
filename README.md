# Work on SVMlight classifier:

* Data formatting : Accuracy : 40%
* Feature extraction : Accuracy : 60%
* Stop words eviction
* Corpus stemming : Accuracy : 89%
* TF-IDF computing : Accuracy : 90.40%
* Least used words eviction
* Bigrams computing : Accuracy : 86%
* Bigrams and unigrams computing : 91.80%
* Improved learning : 98.80%


# format.py

## Usage:
    format.py -d <dic> -i <input> -o <output> (-f|--fun) <fun> [--use-idf]
    [--format <format>]

## Options:
    -h --help       Print this message
    -v --version    Print the version
    -d              The file to print the dictionary
    -i              The input file
    -o              The output file
    -f --fun        Specify the formatting function to use. You can use the
                    following : format_{analyse,analyse_test,train,test}
    --use-idf       Whether or not to compute tf-idf
    --format        Specify the format if needed, the grammar is the following:
                    [target] [separator] [feature][feature_separator][value]
                    [target] has to be a numerical value
                    [feature] has to be a string of alpha-numerical values
                    [value] has to be a numerical value
                    [separator] and [feature_separator] have to be a single non
                    alpha-numerical character.
