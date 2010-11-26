import urllib
import re
import os
import subprocess
import imp

from BeautifulSoup import BeautifulSoup
from settings import DOWNLOADS_FOLDER, PROGRAM_PATH
from utils import remove_html_tags, remove_entities

class Downloader:
    def __init__(self):
        #identify the trackers we can use that exist in the trackers folder
        self._trackers = self._get_trackers()
    
    def _get_trackers(self):
        """Loads tracker files and populates a dict with them"""
        trackers_path = os.path.join(PROGRAM_PATH, 'trackers')
        files = os.listdir(trackers_path)
        tracker_files = [file for file in files if file[-4:] != '.pyc' and file != '__init__.py']
        trackers = []
        for tracker in tracker_files:
            tracker_name = tracker.replace('.py', '')
            trackers.append(tracker_name)           
        return trackers
        
    def download(self, search_term, desired_item_name):     
        """Tries to download something with the desired_item_name from the torrentz results after searching for search_term"""
        good = True
        #TODO: make errors raise exceptions, then handle them
        error_step = ''       
        #TODO: make this a general search call that can take any search site
        #search_results is BeautifulSoup of torrentz.com
        search_results = self._torrentz_search(search_term)        
        #intial_results is a dict of link titles and urls that lead to the 'choose a tracker' page on torrentz
        initial_results =  self._make_initial_results_dict(search_results)
        if initial_results == {}:
            good = False
            error_step = 'make_inital_results_dict'        
        if good:
            #picks out a link we can use 
            desired_link = self._desired_link_from_initial(initial_results, desired_item_name)
            if not desired_link:
                good = False
                error_step = 'desired_link_from_initial'        
        if good:
            #results is a dict of tracker names and url's
            results = self._make_secondary_results_dict(desired_link)
            if results != {}:
                trackers = results.keys()
            else:
                good = False
                error_step = 'make_secondary_results_dict'        
        if good:
            #file_path is the location of the .torrent file or -1 if it didn't work
            file_path = self._download_torrent_file(search_term, desired_item_name, results)
            if not file_path:
                good = False
                error_step = 'download_torrent_file'        
        if good:
            self._open_torrent(file_path)
        else:
            print 'unable to find a valid torrent.'
            print 'problem in: %s' % error_step        
        return 0

    def _download_torrent_file(self, search_term, desired_item_name, results, tracker_number=0):
        #TODO: raise exceptions here if we can't find anything, rather then returning None
        file_path = None
        for tracker, tracker_url in results.items():
            base_file_path = DOWNLOADS_FOLDER
            file_path = base_file_path + desired_item_name.replace(' ', '') + '.torrent'
            print 'downloading from ' + tracker
            #start_url is the torrent's page on the tracker's site
            tracker_file = tracker + ".py"
            tracker_path = os.path.join(PROGRAM_PATH, 'trackers', tracker_file)
            source = imp.load_source('find_url', tracker_path)
            find_url = source.find_url          
            url = find_url(tracker_url, PROGRAM_PATH)         
            if url:
                result = os.system('wget -O "%s" "%s" -t 2 -T 5' % (file_path, url))
                if result != 0:
                    #recursive call if wget is unable to download the .torrent file from the tracker
                    #increments tracker_number so we call the next available tracker
                    file_path = self._download_torrent_file(search_term, desired_item_name, tracker_number+1)
        return file_path
    
    def _torrentz_search(self, search_term):
        """Searches for search_term on torrentz.com and returns the soup that results."""
        print 'getting torrentz results'        
        search_term = search_term.lower()
        split_term = search_term.split()
        url = 'http://www.torrentz.com/feed?q='
        for word in split_term:
            url += word + '+'
        url = url[:-1]
        sock = urllib.urlopen(url)
        html = sock.read()
        sock.close()       
        soup = BeautifulSoup(html)
        print 'done'
        return soup
        
    def _make_initial_results_dict(self, search_results):
        print 'making initial_results_dict'
        initial_result_dict = {}     
        for item in search_results('item'):
            description = str(item.description)
            seeds_index = description.index('Seeds') + 7
            cut_description = description[seeds_index:]
            space_index = cut_description.index(' ')
            seeds = cut_description[:space_index]
            seeds = seeds.replace(",", "")
            seeds = int(seeds)    
            if 'flac' not in str(item.category).lower() and 'wma' not in str(item.category).lower() and seeds >= 5:
                title = item.title
                title = remove_html_tags(str(title))
                title = remove_entities(title)
                #guid is the url of the 'choose a tracker' page on torrentz
                guid = item.guid
                guid = remove_html_tags(str(guid))
                initial_result_dict[title] = guid        
        print 'done'
        return initial_result_dict

    def _desired_link_from_initial(self, initial_results_dict, desired_item_name):
        """Returns a url for the 'choose a tracker' page on torrentz"""
        for result in initial_results_dict:
            if desired_item_name.lower() in result.lower():
                return initial_results_dict[result]
        return None
        
    def _make_secondary_results_dict(self, secondary_results_link):
        print 'making secondary results dict'
        try:
            sock = urllib.urlopen(secondary_results_link)
            html = sock.read()
            sock.close()
        except IOError:
            return {}
            
        soup = BeautifulSoup(html)      
        #all possible links on the page
        possibilities = soup.findAll('a')
        possibilities_dict = {}
        for possibility in possibilities:
            tracker = remove_html_tags(str(possibility)).split()
            if tracker:
                #tracker[0] is the name of the tracker
                tracker = tracker[0].replace('.com', '')
                if tracker in self._trackers:
                    #link is "href="http://whatever.com"
                    link = str(possibility).split()[1]
                    first_quote = link.index('"') + 1
                    second_quote = link.index('"', first_quote)
                    link = link[first_quote:second_quote]
                    #now link is just url of tracker
                    possibilities_dict[tracker] = link      
        print 'done'
        return possibilities_dict
              
    def _open_torrent(self, file_path):
        if os.name == 'posix':
            subprocess.call(('open', file_path))
        elif os.name == 'nt':
            subprocess.call(('start', file_path))
        return 0