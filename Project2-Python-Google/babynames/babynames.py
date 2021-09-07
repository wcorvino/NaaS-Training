#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename, summary):
    """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
    # +++your code here+++
    f = open(filename, "r")
    text = f.read()
    f.close()

    # Extract the year and print it
    year = re.findall(r'Popularity in.*\d\d\d\d', text)
    year[0] = year[0].replace('Popularity in', '')
    year[0] = year[0].replace(' ', '')

    # Extract the names and rank numbers, dupes removed by dictionary
    names = re.findall(r'<td>(\d+).*<td>(\w+).*<td>(\w+)', text)
    mydict = {}
    mylist = []

    for (rank, m, f) in names:
        mydict[m] = rank
        mydict[f] = rank

    # create rank corrections list for dupe names
    for (rank, m, f) in names:
        male = [m, rank]
        if not mydict[m] == rank:
            mylist.append(male)

        female = [f, rank]
        if not mydict[f] == rank:
            mylist.append(female)

    # apply corrections to mydict
    for line in mylist:
        x = line
        mydict[x[0]] = x[1]

    mylist = []
    # create sorted list
    for t in mydict.items():
        mylist.append(t)

    # create text report for output to file
    mytext = ''.join(year) + '\n'
    for t in sorted(mylist):
        mystring = list(t)
        for txt in mystring:
            mytext = mytext + ' ' + str(txt)
        mytext = mytext + '\n'

    # check flag ; create summary files  or just output text
    if summary:
        new_filename = "./" + filename + ".summary"
        print new_filename
        with open(new_filename, "w") as f:
            f.write(mytext)
            f.close()
    else:
        print filename
        print year
        for k, v in sorted(mydict.items(), key=lambda val: val[-1], reverse=False):
            print k + ' ' + str(v)
    return


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)
    # print sys.argv[0], sys.argv[1], sys.argv[2]
    # print args[0], args[1]
    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
        print "Summary"
    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file

    from os.path import exists

    for filename in args:
        if not exists(filename):
            print
            print 'error: check file names and usage.'
            print
            print 'usage: [--summaryfile] file [file ...]'
            print
            sys.exit(1)

    for filename in args:
        extract_names(filename, summary)


if __name__ == '__main__':
    main()
