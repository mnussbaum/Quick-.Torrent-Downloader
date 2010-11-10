#!/usr/bin/env python
import sys
from downloader import Downloader
#import imp
#from settings import program_path
#load = imp.load_source('Downloader', program_path+'downloader.py')
#Downloader = load.Downloader
argv = sys.argv[1:]

if argv:
        search_term = argv[0]
        desired_item_name = argv[1]
else:
        search_term = raw_input('Search Term:')
        desired_item_name = raw_input('Desired Result:') 

downloader = Downloader()
downloader.download(search_term, desired_item_name)
