from trackers.base_tracker import BaseTracker

TRACKER_NAME = "Fenopy"

class Fenopy(BaseTracker):
    def extract_download_url(self, url):
        download_url = '%s==/download.torrent' % url
        return download_url
