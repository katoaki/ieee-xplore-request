#!/usr/bin/env python3

# first import the requests module to be able to send requests
import requests
from lxml import etree
import xml.etree.ElementTree as ET

payload = {}

# asking the user for author
key1 = 'au'
print('Do you want to search for one or more authors? \n'\
      'Type in the names, comma separated, without space. \n'\
      'If not just enter')
keywords1 = input()

# filling the dictionary payload with key and value, if it was input
if keywords1:
    value1 = keywords1.split(',')
    payload[key1] = value1

# search for keywords in title
key2 = 'ti'
print('Do you want to search for keywords in the title? \n'\
      'Input now or press Enter:')
keywords2 = input()
if keywords2:
    value2 = keywords2.split(',')
    payload[key2] = value2

# search for keywords in everything: title, abstract, document
key3 = 'querytext'
print('If you want to search for keywords in the title, abstract and document, \n'\
      'enter the keywords here. IEEE xplore allows a maximum of 10 keywords.')
keywords3 = input()
if keywords3:
    value3 = keywords3.split(',')
    payload[key3] = value3

# start year to search in publications
key4 = 'pys'
print('Year to start the search from:')
value4 = input()
if value4:
    payload[key4] = value4


# end year to search in publications
key5 = 'pye'
print('Year until to search for publications:')
value5 = input()
if value5:
    payload[key5] = value5

key6 = 'rs'
value6 = 1
payload[key6] = value6
key7 = 'hc'
value7 = 1000
payload[key7] = value7

# test to see how payload looks like
print(payload)

# try to assemble the request url a little more automatically by passing parameters with params
r = requests.get('http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?',
                 params=payload)

# test if the url is assembled right
print(r.url)

# z contains all the entries (maximum 1000) of the first request response
z = r

# XML strings to etree
z_root = etree.fromstring(z.content)

# XML strings to etree
#r_root = etree.fromstring(r.content)

# find the total number of entries with the parameters and keywords I searched for
for totalfound in z_root.findall('totalfound'):
	total = totalfound.text
	print('total search results= ',total)

# generate parameters for getting all the search results
total = int(total)
rs = 1
while total > 1000:
#    print('rs = ', rs)
    rs = rs + 1000
    value6 = rs
    payload[key6] = value6
#    print(payload)
    r = requests.get('http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?',
	params=payload)
    r_root = etree.fromstring(r.content)
    z_root.append(r_root)
#    print(r.url)
    total = total - 1000
#    print('total = ', total)

# put all articlenumbers from z_root in an array for easier access
articleArray = []
for arnumber in z_root.findall('.//arnumber'):
    articleArray.append(arnumber.text)

# access the html website to each articlenumber and in the future search for additional information
#htmlsuche = requests.get('http://ieeexplore.ieee.org/xpls/icp.jsp?',params=payload)

#write data into an output file
#tree = ET.ElementTree(z_root)
#tree.write('output.xml')
