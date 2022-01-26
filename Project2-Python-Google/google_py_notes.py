#!/usr/bin/python2 -tt
import sys
import os
import commands


def x_list(local_dir):
    filenames = os.listdir(local_dir)
    for filename in filenames:
        path = os.path.join(local_dir, filename)
        print path
        print os.path.abspath(path)
    return


def x_list1(local_dir):
    cmd = 'ls -l ' + local_dir
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        print sys.stderr('there was an error', output)
        sys.exit(1)
    print output
    return


#os.path.exists()
#os.path.mkdir

#import shutil
#shutil.copy(source,destination)
#minute 18, find spec file and list, copy sepcial files to dir, then zip

def main():
    x_list('./basic')#sys.argv[1]
    x_list1('./basic')
