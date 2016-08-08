#!/usr/bin/env python3

# first import the requests module to be able to send requests
import requests
payload = {}

# asking the user for author
searchtype1 = 'au'
print('Do you want to search for one or more authors? Type in the names, comma separated, without space. If not just enter')
keywords1 = input()

# filling the dictionary payload with searchtype and key, if it was input
if keywords1:
    key1 = keywords1.split(',')
    payload[searchtype1] = key1

# search for keywords in title
searchtype2 = 'ti'
print('Do you want to search for keywords in the title? Input now or press Enter:')
keywords2 = input()
if keywords2:
    key2 = keywords2.split(',')
    payload[searchtype2] = key2

# search for keywords in everything: title, abstract, document
searchtype3 = 'querytext'
print('If you want to search for keywords in the title, abstract and document, enter the keywords here. IEEE xplore allows a maximum of 10 keywords.')
keywords3 = input()
if keywords3:
    key3 = keywords3.split(',')
    payload[searchtype3] = key3

# start year to search in publications
searchtype4 = 'pys'
print('Year to start the search from:')
key4 = input()
if key4:
    payload[searchtype4] = key4


# end year to search in publications
searchtype5 = 'pye'
print('Year until to search for publications:')
key5 = input()
if key5:
    payload[searchtype5] = key5

searchtype6 = 'rs'
key6 = 1
payload[searchtype6] = key6
searchtype7 = 'hc'
key7 = 1000
payload[searchtype7] = key7

# test to see how payload looks like
print(payload)

# try to assemble the request url a little more automatically by passing parameters with params
r = requests.get('http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?', params=payload)

# test if the url is assembled right
print(r.url)


# show the response to the request
print(r.text)
