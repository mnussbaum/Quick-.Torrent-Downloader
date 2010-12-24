#!/usr/bin/env python
import sys

from downloader import Downloader

def main(args):
    if args:
        search_term = args[0]
        desired_item_name = args[1]
    else:
        search_term = raw_input('Search Term: ')
        desired_item_name = raw_input('Item to Find: ')
    downloader = Downloader()
    downloader.download(search_term, desired_item_name)
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
