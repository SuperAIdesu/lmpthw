import argparse

parser = argparse.ArgumentParser(description="A replica of GNU *cut*")
parser.add_argument("-d", "--delimiter", default="\t")
parser.add_argument("-f", "--fields")
parser.add_argument("file")
args = parser.parse_args()

fileobj = open(args.file, "r")
startnum = int(args.fields.split("-")[0])
endnum = int(args.fields.split("-")[1])
for line in fileobj:
    line = line.strip("\n")
    lineslice = line.split(args.delimiter)
    for i in range(startnum, endnum+1):
        print(lineslice[i-1], end=" ")
    print("\n", end="")
