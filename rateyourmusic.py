from bs4 import BeautifulSoup
import urllib2
import re

opener = urllib2.build_opener()
opener.addheaders = [
        ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                       'Windows NT 5.2; .NET CLR 1.1.4322)'))]

rym_url = "http://rateyourmusic.com/charts/top/album/all-time"
rym_source = opener.open(rym_url)
rym_soup = BeautifulSoup(rym_source)

artists = []
albums = []

# for result in rym_soup.find_all("a", "artist"):
# 	print result.string
# print rym_soup.title.string
for result in rym_soup.find_all("a", "album"):
	print result.string