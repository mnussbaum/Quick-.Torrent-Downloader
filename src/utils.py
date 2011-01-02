import re
from htmlentitydefs import name2codepoint

from errors import DownloaderError

def write_file(file_path, data):
    out_file = open(file_path, 'w')
    out_file.write(data)
    out_file.close()

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def remove_entities(word):
    word = word.replace("&#039;", "'")
    return word
