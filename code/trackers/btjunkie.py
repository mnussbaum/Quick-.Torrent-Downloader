import re

from trackers.base_tracker import BaseTracker

TRACKER_NAME = "Btjunkie"

class Btjunkie(BaseTracker):
    def extract_download_url(self, url):
        name = url[7:]
        download_url = 'http://dl.%s/download.torrent' % name
        return download_url
