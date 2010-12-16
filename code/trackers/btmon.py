from trackers.base_tracker import BaseTracker

class Tracker(BaseTracker):
    def __init__(self):
        self.name = 'Btmon'

    def extract_download_url(self, url):
        download_url = url[:-5]
        return download_url
