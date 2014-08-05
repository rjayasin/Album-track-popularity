'''
This particular module is going to be "deprecated", as its development has hit
a standstill and also because I'd like to focus on the other aspects of this 
project. 
I may return to it later.
'''

from __future__ import unicode_literals
import sys
import codecs
import urllib2
import re
from bs4 import BeautifulSoup

# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
opener = urllib2.build_opener()
opener.addheaders = [
        ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                       'Windows NT 5.2; .NET CLR 1.1.4322)'))]

rym_url = "http://rateyourmusic.com/charts/top/album/all-time"
rym_source = opener.open(rym_url)
rym_soup = BeautifulSoup(rym_source)

artists = []
albums = []

for result in rym_soup.find_all("a", "artist"):
	artists.append(result.string)
for result in rym_soup.find_all("a", "album"):
	albums.append(result.string)

# print artists
probablywrong = zip(artists, albums)
print probablywrong