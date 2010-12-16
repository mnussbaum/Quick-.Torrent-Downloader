import urllib2

from BeautifulSoup import BeautifulSoup

from trackers.base_tracker import BaseTracker
from errors import DownloaderError
from utils import remove_html_tags

class Tracker(BaseTracker):
    def __init__(self):
        self.name = 'ThePirateBay'

    def extract_download_url(self, url):
        start_index = url.index('torrent')
        start_index += 8
        pirate_num = url[start_index:]
        pirate_title = self._pirate_title(url)
        if not pirate_title:
            raise DownloaderError('Unable to parse tracker site')
        download_url = 'http://torrents.thepiratebay.org/'+\
          '%s/%s.%s.TPB.torrent' % (pirate_num, pirate_title, pirate_num)
        return download_url

    def _pirate_title(self, url):
        try:
            sock = urllib2.urlopen(url)
            html = sock.read()
            sock.close()
        except URLError:
            raise DownloaderError('Connection issue')
        soup = BeautifulSoup(html)
        title = soup.find('div', {'id':'title'})
        pirate_title = None
        if title:
            formatted_title = str(title)
            formatted_title = remove_html_tags(formatted_title)
            formatted_title = formatted_title.strip()
            formatted_title = formatted_title.replace(',', '_')
            pirate_title = formatted_title.replace(' ', '_')
        return pirate_title
