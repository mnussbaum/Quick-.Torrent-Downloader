import re

from trackers.base_tracker import BaseTracker

class Tracker(BaseTracker):
    def __init__(self):
        self.name = 'BTJunkie'

    def extract_download_url(self, url):
        name = url[7:]
        download_url = 'http://dl.%s/download.torrent' % name
        return download_url
