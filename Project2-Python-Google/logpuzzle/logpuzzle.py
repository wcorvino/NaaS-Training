#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
    # +++your code here+++
    f = open(filename, "r")
    text = f.read()
    f.close()

    url_list = ','.join(re.findall(r'GET (\S+.*jpg)', text))
    url_list = url_list.split(',')
    url_list = set(url_list)
    url_list = list(url_list)

    for i in range(0, len(url_list)):
        url_list[i] = "http://code.google.com" + url_list[i]
        # debug print url_list[i]

    url_dict = {}
    for url in url_list:
        url_dict[url] = re.findall(r'-(\w\w\w\w).jpg', url)

    url_list = []
    for k, v in sorted(url_dict.items(), key=lambda val: val[-1], reverse=False):
        url_list.append(k)

    return url_list


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
    # +++your code here+++
    try:
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)
    except ValueError:
        print "Directory {dest_dir} already exists"

    image_seq = "<html>\n"
    image_seq = image_seq + '<body>\n'
    seq_no = 0
    for url in img_urls:
        file_path = os.path.abspath('.') + '/' + dest_dir + '/image' + str(seq_no) + ".jpg"
        urllib.urlretrieve(url, file_path)
        #
        s = 'image' + str(seq_no) + ".jpg"
        print s
        #
        s = '<img src="./' + s + '">'
        image_seq = image_seq + s
        #
        seq_no = seq_no + 1
    image_seq = image_seq + '</body>\n'
    image_seq = image_seq + '</html>\n'
    # debug print image_seq

    index_filename = os.path.abspath('.') + '/' + dest_dir + '/index.html'
    with open(index_filename, "w") as f:
        f.write(image_seq)
        f.close()
    return


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)


if __name__ == '__main__':
    main()
