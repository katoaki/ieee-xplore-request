#!/usr/bin/env python3

#import the right packages
import requests
from lxml import etree
import xml.etree.ElementTree as ET

# get an xml from a website
r = requests.get('http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?querytext=java&au=Wang&hc=10&rs=11&sortfield=ti&sortorder=asc')
print(r.url)
print(r.text)

# trying to parse directly request response
root = ET.fromstring(r.content)

#parsing my xml-file (unfortunately not yet from the request directly
#tree = ET.parse("response.xml")
#root = tree.getroot()

# find the total number of entries with the parameters and keywords I searched for
for totalfound in root.findall('totalfound'):
	total = totalfound.text
	print(total)

# generate parameters for getting all the search results
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

# get the articlenumbers from the xml-file to reach the html version of articles
for arnumber in root.findall('.//arnumber'):
        articlenumber = arnumber.text
        print(articlenumber)
                




