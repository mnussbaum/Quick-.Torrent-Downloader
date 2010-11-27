from trackers.tracker import Tracker

TRACKER_NAME = "Btmon"

class Btmon(Tracker):
    def extract_download_url(self, url):
        download_url = url[:-5]
        return download_url
