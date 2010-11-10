tracker = 'btjunkie.org'

def find_url(start_url, program_path):
	name = start_url[7:]
	url = 'http://dl.' + name + '/download.torrent'
	
	return url
	
	