import argparse
import glob
import sys
import os.path

parser = argparse.ArgumentParser(description="replica of GNU *find*")
parser.add_argument("dir", nargs=1, help="dir to start find")
parser.add_argument("-name", help="find by name")
parser.add_argument("-type", help="find by type")
parser.add_argument("-print", action="store_true", help="print file name")
parser.add_argument("-exec", nargs="*", help="execute a command")
args = parser.parse_args()


def findfile(args):
    if args.name is not None:
        for file in glob.glob(args.dir[0]+args.name):
            execarg(args, file)
        return 0

    if args.type == "d":
        for dirres in glob.glob(args.dir[0]+"*"):
            if os.path.isdir(dirres):
                execarg(args, dirres)
        return 0

    if args.type == "f":
        for file in glob.glob(args.dir[0]+"*"):
            if os.path.isfile(file):
                execarg(args, file)
        return 0


def execarg(args, file):
    if args.print:
        print(file)

    if args.exec is not None:
        command = " ".join(args.exec)
        donecommand = command.replace("{}", file)
        os.system(donecommand)


# print(args.dir[0]+"*")
findfile(args)
sys.exit(0)
