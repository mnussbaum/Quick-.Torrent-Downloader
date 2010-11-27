import re

from trackers.tracker import Tracker

TRACKER_NAME = "Torrenthound"

class Torrenthound(Tracker):
    def extract_download_url(self, url):
        p = re.compile('/hash/')
        mid_url = p.sub('/torrent/', url, 1)
        download_url = mid_url[:mid_url.index('/torrent-info')]
        return download_url
