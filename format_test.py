#!/usr/bin/python3

import sys
import format as frmt
from collections import OrderedDict


if __name__ == "__main__":
    script, f_in, f_out = sys.argv
    lines = frmt.read_file(f_in)
    dic = frmt.read_dic("train.dict")
    #for key, value in dic.items():
    #    print("{0} : {1}".format(key, str(value)))
    frmt.format_data(f_out, lines, dic)
