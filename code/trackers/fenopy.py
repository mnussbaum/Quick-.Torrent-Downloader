from trackers.base_tracker import BaseTracker

class Tracker(BaseTracker):
    def __init__(self):
        super(Tracker, self).__init__()
        self.name = 'Fenopy'

    def extract_download_url(self, url):
        download_url = '%s==/download.torrent' % url
        return download_url
