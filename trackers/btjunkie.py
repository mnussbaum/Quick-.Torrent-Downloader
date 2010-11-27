import re

from trackers.tracker import Tracker

TRACKER_NAME = "Btjunkie"

class Btjunkie(Tracker):
    def extract_download_url(self, url):
        name = url[7:]
        download_url = 'http://dl.%s/download.torrent' % name
        return download_url
