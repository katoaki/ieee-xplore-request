#!/usr/bin/env python3

# first import the requests module to be able to send requests
#from lxml import etree
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

#root = ET.fromstring(IEEErequest)

root.tag
root.attrib

for child in root:
    print(child.tag, child.attrib)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
