from trackers.tracker import Tracker

TRACKER_NAME = "Fenopy"

class Fenopy(Tracker):
    def extract_download_url(self, url):
        download_url = '%s==/download.torrent' % url
        return download_url
