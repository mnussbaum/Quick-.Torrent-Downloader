import os
import sys

#get proper paths
split_path = os.path.abspath(__file__).split('/')
downloader_index = split_path.index('downloader')
path = '/'
for directory in split_path[:downloader_index]:
    path = os.path.join(path, directory)
path = os.path.join(path, 'downloader/code/trackers/')
sys.path.append(path)


from base_tracker import BaseTracker

class Tracker(BaseTracker):
    def __init__(self):
        super(Tracker, self).__init__()
        self.name = "FakeTracker"

    def extract_download_url(self, start_url):
        return start_url
