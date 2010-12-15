import sys

TRACKER_NAME = 'BaseTracker'

class BaseTracker(object):
    '''Basic tracker object to be subclassed. Takes the url
    of a torrent page from the tracker and returns the url of
    the downloadable .torrent file'''
    def __init__(self):
        pass

    def extract_download_url(self, url):
        return url
