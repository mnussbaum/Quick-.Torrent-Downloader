#!/usr/bin/env python
import sys
import imp
from settings import program_path
load = imp.load_source('download_pitchfork_best_new_albums', program_path+'find_music.py')
download_pitchfork_best_new_albums = load.download_pitchfork_best_new_albums

argv = sys.argv[1:]
if argv:
	number_of_albums = argv[0]
else:
	number_of_albums = 10

download_pitchfork_best_new_albums(int(number_of_albums))
