import urllib2
import sys
import unittest
from mock import patch, Mock

from test_path import DOWNLOADER_PATH
sys.path.append(DOWNLOADER_PATH)

import downloader
from errors import DownloaderError
from test_resources.general_search_results import search_results
from test_resources.tracker_results import tracker_results
from BeautifulSoup import BeautifulSoup

FakeSearchSock = Mock()
FakeSearchSock.read = Mock(return_value=search_results)
FakeSearchUrlOpen = Mock(return_value=FakeSearchSock)
FakeTrackerSock = Mock()
FakeTrackerSock.read = Mock(return_value=tracker_results)
FakeTrackerUrlOpen = Mock(return_value=FakeTrackerSock)
FakeEmptySock = Mock()
FakeEmptySock.read = Mock(return_value='')
FakeEmptyUrlOpen = Mock(return_value=FakeEmptySock)

class DownloaderTest(unittest.TestCase):
    def setUp(self):
        self._mock_listdir = Mock(return_value=['test.py'])
        self._fake_soup = BeautifulSoup(search_results)
        self._correct_parsed_results = \
        {'The Beatles Greatest Hits Remastered/2009/MP3 Bubanee':
        'http://www.torrentz.com/0898a4b562c1098eb69b9b801c61a51d788df0f5'}
        self._correct_link = 'http://www.torrentz.com/0898a4b562c109' + \
          '8eb69b9b801c61a51d788df0f5'
        self._correct_trackers = {
          'torrenthound': 'http://www.torrenthound.com/hash/0898a4b5' + \
            '62c1098eb69b9b801c61a51d788df0f5/torrent-info/The-Beatl' + \
            'es-2009-Greatest-Hits-CDRip-Remastered-Bubanee-',
          'btmon': 'http://www.btmon.com/Audio/Unsorted/The_Beatles_' + \
            '2009_Remastered_Greatest_Hits_41_Songs_CDRips_Bubanee.t' + \
            'orrent.html',
          'btjunkie': 'http://btjunkie.org/torrent/The-Beatles-Great' + \
            'est-Hits-Remastered-2009-MP3-Bubanee/43580898a4b562c109' + \
            '8eb69b9b801c61a51d788df0f5',
          'thepiratebay': 'http://thepiratebay.org/torrent/5079924',
          'fenopy': 'http://fenopy.com/torrent/The+Beatles+2009+Grea' + \
            'test+Hits+41+Songs+CDRip+Remastered+/MzYzODQxMA'}
        self._downloader_ut = downloader.Downloader()
        
    def test_get_trackers(self):
        with patch('os.listdir', self._mock_listdir):
            trackers = self._downloader_ut._get_trackers()
            self.assertEqual(['test'], trackers)
   
    @patch.object(urllib2, 'urlopen', FakeSearchUrlOpen)  
    def test_torrentz_search(self):
        search_term = 'TeSt QuERY'
        result = self._downloader_ut._torrentz_search(search_term)
        self.assertEquals(self._fake_soup, result)
        
    def test_parse_general_search_results__good_results(self):
        parsed_results = \
          self._downloader_ut._parse_general_search(self._fake_soup)
        self.assertEquals(self._correct_parsed_results, parsed_results)
        
    def test_parse_general_search_results__bad_results(self):
        empty_soup = BeautifulSoup('<html></html>')
        self.assertRaises(DownloaderError,
          self._downloader_ut._parse_general_search, empty_soup)
          
    def test_general_results_link__good_result(self):
        parsed_results = \
          self._downloader_ut._parse_general_search(self._fake_soup)
        link = \
          self._downloader_ut._general_result_link(parsed_results,
          'tHe bEatlEs')
        self.assertEquals(self._correct_link, link)
          
    def test_general_results_link__bad_result(self):
        parsed_results = \
          self._downloader_ut._parse_general_search(self._fake_soup)
        self.assertRaises(DownloaderError,
          self._downloader_ut._general_result_link, parsed_results,
          'huh?')
          
    @patch.object(urllib2, 'urlopen', FakeTrackerUrlOpen)  
    def test_find_trackers__good_results(self):
        found_trackers = \
          self._downloader_ut._find_trackers(self._correct_link)
        self.assertDictEqual(self._correct_trackers, found_trackers)
        
    @patch.object(urllib2, 'urlopen', FakeEmptyUrlOpen)  
    def test_find_trackers__bad_results(self):
          self.assertRaises(DownloaderError,
            self._downloader_ut._find_trackers, 'http://nada.com')
