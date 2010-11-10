tracker = 'thepiratebay.org'

def find_url(start_url, program_path):
	import imp
	load = imp.load_source('remove_html_tags', program_path+'utils.py')
	remove_html_tags = load.remove_html_tags
	
	start_index = start_url.index('torrent')
	start_index += 8
	tracker_num = start_url[start_index:]
	
	#load BeautifulSoup to get the name of the torrent for the download url
	import imp
	source = imp.load_source('BeautifulSoup', program_path)
	BeautifulSoup = source.BeautifulSoup
	
	import urllib
	sock = urllib.urlopen(start_url)
	html = sock.read()
	sock.close()
		
	soup = BeautifulSoup(html)
	
	title = soup.find('div', {'id':'title'})
	url = None
	if title:
		title = str(title)
		title = remove_html_tags(title)
		title = title.strip()
		title = title.replace(',', '_')
		title = title.replace(' ', '_')
		tracker_name = title
				
		url = 'http://torrents.thepiratebay.org/'+tracker_num+'/'+tracker_name+'.'+tracker_num+'.TPB.torrent'
	return url