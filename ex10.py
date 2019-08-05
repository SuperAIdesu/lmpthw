# -d -i -M -n not completed
import argparse
import sys
from functools import cmp_to_key


def argproc():  # process cmd args
    parser = argparse.ArgumentParser(
            description="A degraded replica of GNU *sort*")
    parser.add_argument('-b', '--ignore-leading-blanks', action="store_true")
    # parser.add_argument('-c', '--check', action="store_true")
    parser.add_argument('-d', '--dictionary-order', action="store_true")
    parser.add_argument('-f', '--ignore-case', action="store_true")
    parser.add_argument('-i', '--ignore-nonprinting', action="store_true")
    parser.add_argument('-M', '--month-sort', action="store_true")
    parser.add_argument('-n', '--numeric-sort', action="store_true")
    parser.add_argument('-r', '--reverse', action="store_true")
    parser.add_argument("file", default='-', nargs='?')
    return parser.parse_args()


def fileproc(args):  # open file, use stdin if not specified
    if args.file == '-':
        fileobj = sys.stdin
    else:
        fileobj = open(args.file, "r")
    return fileobj


# functions for comparing two str
def compf_b(str1, str2):
    return compf_default(str1.lstrip(), str2.lstrip())


def compf_d(str1, str2):
    pass


def compf_f(str1, str2):
    return compf_default(str1.upper(), str2.upper())


def compf_i(str1, str2):
    pass


def compf_M(str1, str2):
    pass


def compf_n(str1, str2):
    pass


def compf_default(str1, str2):
    if str1 > str2:
        return 1
    elif str1 == str2:
        return 0
    else:
        return -1


# sort and print. args: file, function used for comparing, reverse(True/False)
def sortproc(fileobj, compf, reverse):
    lineslist = fileobj.readlines()
    lineslist.sort(key=cmp_to_key(compf), reverse=reverse)
    for i in lineslist:
        print(i, end='')


args = argproc()
fileobj = fileproc(args)

if args.ignore_leading_blanks:
    compf = compf_b
elif args.dictionary_order:
    compf = compf_d
elif args.ignore_case:
    compf = compf_f
elif args.ignore_nonprinting:
    compf = compf_i
elif args.month_sort:
    compf = compf_M
elif args.numeric_sort:
    compf = compf_n
else:
    compf = compf_default

sortproc(fileobj, compf, args.reverse)
