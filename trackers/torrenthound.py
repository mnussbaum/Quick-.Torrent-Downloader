tracker = 'torrenthound.com'

def find_url(start_url, program_path):
	import re
	
	p = re.compile('/hash/')
	mid_url = p.sub('/torrent/', start_url, 1)
	url = mid_url[:mid_url.index('/torrent-info')]
	
	return url					