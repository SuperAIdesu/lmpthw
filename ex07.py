import re
import argparse
import sys
from termcolor import colored

parser = argparse.ArgumentParser(description="A replica of GNU *grep*")
parser.add_argument("pattern")
parser.add_argument("file", default="-", nargs='?')
args = parser.parse_args()


def grep_file(args):
    fileobj = open(args.file, "r")
    regobj = re.compile(args.pattern)
    for line in fileobj:
        matchobj = regobj.search(line)
        if matchobj:
            print(line[:matchobj.start()] +
                  colored(line[matchobj.start():matchobj.end()], "red") +
                  line.strip("\n")[matchobj.end():])


def grep_stdin(args):
    regobj = re.compile(args.pattern)
    for line in sys.stdin:
        matchobj = regobj.search(line)
        if matchobj:
            print(line[:matchobj.start()] +
                  colored(line[matchobj.start():matchobj.end()], "red") +
                  line.strip("\n")[matchobj.end():])


if args.file == "-":
    grep_stdin(args)
else:
    grep_file(args)
