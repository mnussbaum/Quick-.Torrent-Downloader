import re
from htmlentitydefs import name2codepoint

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def remove_entities(word):
	word = word.replace("&#039;", "'")
	return word