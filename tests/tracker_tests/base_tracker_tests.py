import sys
import os
import unittest

#get proper paths
split_path = os.path.abspath(__file__).split('/')
downloader_index = split_path.index('downloader')
path = '/'
for directory in split_path[:downloader_index]:
    path = os.path.join(path, directory)
path = os.path.join(path, 'downloader/src/trackers/')
sys.path.append(path)

from base_tracker import BaseTracker

class TestBaseTracker(unittest.TestCase):
    def setUp(self):
        self._base_tracker_ut = BaseTracker()

    def test_name(self):
        self.assertEquals('BaseTracker', self._base_tracker_ut.name)

    def test_extract_url(self):
        self.assertEquals('test',
          self._base_tracker_ut.extract_download_url('test'))
