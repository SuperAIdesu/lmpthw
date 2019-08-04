import argparse

parser = argparse.ArgumentParser(
                                 description='A replica of Unix *cat*')
parser.add_argument('filename', nargs='+', metavar='filename')
args = parser.parse_args()
filename = args.filename

for i in range(len(filename)):
    fileobj = open(filename[i], mode='r')
    print(fileobj.read())
