import argparse
import re
import sys


def argproc():
    parser = argparse.ArgumentParser(
            description="A degraded replica of GNU *sed*, only s expression")
    parser.add_argument("pattern")
    parser.add_argument("file")
    return parser.parse_args()


def sed_s(slicedcommand, fileobj):
    patternobj = re.compile(slicedcommand[1])
    for line in fileobj:
        matchobj = patternobj.search(line)
        if matchobj:
            print(line[:matchobj.start()] +
                  slicedcommand[2] + line[matchobj.end():], end="")
        else:
            print(line, end="")


args = argproc()
fileobj = open(args.file, "r")
slicedcommand = args.pattern.split('/')

if slicedcommand[0] == 's':
    sed_s(slicedcommand, fileobj)
else:
    print("Not Supported")
    sys.exit(1)
