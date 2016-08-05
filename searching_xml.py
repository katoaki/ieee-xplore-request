#!/usr/bin/env python3

# first import the requests module to be able to send requests
#from lxml import etree
#from io import StringIO, BytesIO

#tree = etree.parse('response.xml')

#import requests


# make a request
#r = requests.get('http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?querytext=canary')

# test if the url is assembled right
#print(r.url)


# show the response to the request
#print(r.text)

#tree = etree.parse("response.xml")
#root = parser.close()
#print (root.tag)

import xml.etree.ElementTree as ET
tree = ET.parse("response.xml")
root = tree.getroot()

# find the total number of entries with the parameters and keywords I searched for
for totalfound in root.findall('totalfound'):
	total = totalfound.text
	print(total)

total = int(total)

rs = 1

while total > 1000:
    print('rs = ', rs)
    hc = 1000
    print('hc = ', hc)
    rs = rs + 1000
    total = total - 1000
    print('total = ', total)
hc = total
print('hc = ', hc)

import lxml
from lxml.html.clean import Cleaner

cleaner = Cleaner()
cleaner.remove_tags = ['<![CDATA[]]>']
