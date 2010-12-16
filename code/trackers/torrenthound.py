import re

from trackers.base_tracker import BaseTracker

class Tracker(BaseTracker):
    def __init__(self):
        super(Tracker, self).__init__()
        self.name = 'TorrentHound'

    def extract_download_url(self, url):
        p = re.compile('/hash/')
        mid_url = p.sub('/torrent/', url, 1)
        download_url = mid_url[:mid_url.index('/torrent-info')]
        return download_url
