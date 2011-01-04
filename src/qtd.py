#!/usr/bin/env python
import getopt
import sys

from downloader import Downloader

def main():
    usage = "Please use -s to specify a search term, and -r to specify" + \
      " the desired result name"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:r:h")
    except getopt.GetoptError:
        print usage
        sys.exit(1)
    search_term = None
    desired_item_name = None
    for opt, arg in opts:
        if opt == '-s':
            search_term = arg
        elif opt == '-r':
            desired_item_name = arg
        elif opt == '-h':
            print usage
            return 0
    if not desired_item_name or not search_term:
        try:
            search_term = raw_input('Search Term: ')
            desired_item_name = raw_input('Desired Item Name: ')
        except EOFError:
            return 0
    downloader = Downloader()
    downloader.download(search_term, desired_item_name)
    return 0

if __name__ == "__main__":
    main()
