import re
import argparse
from termcolor import colored

parser = argparse.ArgumentParser(description="A replica of GNU *grep*")
parser.add_argument("pattern")
parser.add_argument("file")
args = parser.parse_args()

fileobj = open(args.file, "r")
regobj = re.compile(args.pattern)
for line in fileobj:
    matchobj = regobj.search(line)
    if matchobj:
        print(line[:matchobj.start()] +
              colored(line[matchobj.start():matchobj.end()], "red") +
              line.strip("\n")[matchobj.end():])
