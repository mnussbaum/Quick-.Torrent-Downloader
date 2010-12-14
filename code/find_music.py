from BeautifulSoup import BeautifulSoup
import urllib
from odict import OrderedDict
import imp

from settings import program_path
load = imp.load_source('Downloader', program_path+'downloader.py')
Downloader = load.Downloader
load = imp.load_source('remove_html_tags', program_path+'utils.py')
remove_html_tags = load.remove_html_tags

def get_pitchfork_best_new_albums_dict():
	print 'getting albums feed'
	url = 'http://feeds.feedburner.com/PitchforkBestNewAlbums?format=xml'
	sock = urllib.urlopen(url)
	html = sock.read()
	sock.close()
		
	soup = BeautifulSoup(html)
	
	titles = soup('title')
	titles.pop(0)
	albums_dict = OrderedDict()
	for title in titles:
		title = remove_html_tags(str(title))
		split_title = title.split()
		artist = ''
		album = ''
		dash_found = False
		for word in split_title:
			if word == '-':
				dash_found = True
				artist = artist.rstrip()
			if dash_found == False:
				artist += word + ' '
			if dash_found == True:
				album += word + ' '
		album = album[2:-1]
		albums_dict[artist] = album
	print 'done'
			
	return albums_dict

def download_pitchfork_best_new_albums(number_of_albums):
	best_new_albums = get_pitchfork_best_new_albums_dict()
	download_count = 0
	downloader = Downloader()
	for artist in best_new_albums:
		if download_count <= number_of_albums:
			print 'downloading ' + str(artist)
			album = best_new_albums[artist]
			downloader.download(artist+" "+album, album)
			download_count += 1
	return 0
