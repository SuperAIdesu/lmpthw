import argparse
import sys


def argproc():  # process cmd args
    parser = argparse.ArgumentParser(
            description="A degraded replica of GNU *uniq*")
    parser.add_argument("file", default='-', nargs='?')
    return parser.parse_args()


def fileproc(args):  # open file, use stdin if not specified
    if args.file == '-':
        fileobj = sys.stdin
    else:
        fileobj = open(args.file, "r")
    return fileobj


args = argproc()
fileobj = fileproc(args)
lineslist = fileobj.readlines()
print(lineslist[0], end='')
for i in range(1, len(lineslist)):
    if lineslist[i] != lineslist[i-1]:
        print(lineslist[i], end='')
