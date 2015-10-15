__author__ = 'YunongLiu'

# test if this file can be sync to vm
from urllib2 import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print (html.read())