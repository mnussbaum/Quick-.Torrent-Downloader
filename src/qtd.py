#!/usr/bin/env python
import getopt
import sys

from downloader import Downloader

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:r:")
    except getopt.GetoptError:
        print "Please use -s to specify a search term, and -r to specify the desired result name"
        sys.exit(1)
    search_term = None
    desired_item_name = None
    for opt, arg in opts:
        if opt == '-s':
            search_term = arg
        elif opt == '-r':
            desired_item_name = arg
    if not desired_item_name or not search_term:
        search_term = raw_input('Search Term: ')
        desired_item_name = raw_input('Item to Find: ')
    downloader = Downloader()
    downloader.download(search_term, desired_item_name)
    return 0

if __name__ == "__main__":
    main()
