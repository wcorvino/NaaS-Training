#!/usr/bin/python2.x -tt
#google python training

import sys

def Cat(filename):
    f = open(filename, "rU")
    for line in f:
      print line, #printing one line at a time from the open file
    # lines = f.readlines(), read entire file into memory as a list of lines,  then print lines
    # lines = f.read(), read the entire file into memory as a single string, then print lines ( for regex)

    f.close()

# Define a main() function that prints greeting
def main():
   Cat(sys.argv[1])

# This is the standard boiler plate that calls the main() fucntion.
if __name__ == '__main__':

    main()
