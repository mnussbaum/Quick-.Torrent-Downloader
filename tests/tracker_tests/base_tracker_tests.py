import sys
import os
import unittest
from mock import Mock, patch

#get proper paths
split_path = os.path.abspath(__file__).split('/')
downloader_index = split_path.index('downloader')
path = '/'
for directory in split_path[:downloader_index]:
    path = os.path.join(path, directory)
path = os.path.join(path, 'downloader/code/trackers/')
sys.path.append(path)

from base_tracker import BaseTracker

class TestBaseTracker(unittest.TestCase):
    def setUp(self):
        self._base_tracker_ut = BaseTracker()

    def test_tracker_name(self):
        tracker_name = self._base_tracker_ut.TRACKER_NAME
        self.assertTrue(tracker_name)
