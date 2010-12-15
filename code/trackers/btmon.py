from trackers.base_tracker import BaseTracker

TRACKER_NAME = "Btmon"

class Btmon(BaseTracker):
    def extract_download_url(self, url):
        download_url = url[:-5]
        return download_url
