#!/usr/bin/env python3

#import the right packages
import requests
from lxml import etree
import xml.etree.ElementTree as ET

# get an xml from a website
r = requests.get('http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?rs=1&hc=1000&ti=reliability&querytext=Copper')
#print(r.url)
#print(r.text)

# z contains all the entries (maximum 1000) of the first request response
z = r

r = requests.get('http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?rs=1001&hc=1000&ti=reliability&querytext=Copper')
#print(r.url)
#print(r.text)

# XML strings to etree
z_root = etree.fromstring(z.content)
r_root = etree.fromstring(r.content)

# append the r to z
z_root.append(r_root)

# print the new XML document, which is z
#print(etree.tostring(z_root))
#tree = ET.ElementTree(z_root)

#write data into an output file
#tree.write('output.xml')

#trying to parse directly request response
#root = ET.fromstring(z.content)

#parsing my xml-file (unfortunately not yet from the request directly
#tree = ET.parse("output.xml")
#root = tree.getroot()

# find the total number of entries with the parameters and keywords I searched for
for totalfound in z_root.findall('totalfound'):
	total = totalfound.text
	print(total)

# generate parameters for getting all the search results
#total = int(total)

#rs = 1

#while total > 1000:
#    print('rs = ', rs)
#    hc = 1000
#    print('hc = ', hc)
#    rs = rs + 1000
#    total = total - 1000
#    print('total = ', total)
#hc = total
#print('hc = ', hc)

# get the articlenumbers from the xml-file to reach the html version of articles
#for arnumber in root.findall('.//arnumber'):
#        articlenumber = arnumber.text
#        print(articlenumber)
                




