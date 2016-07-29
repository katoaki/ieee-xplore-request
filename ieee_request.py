#!/usr/bin/env python3

# first import the requests module to be able to send requests
import requests

#define initialize variables for search parameters and the corresponding keywords

# asking for author
print('If you want to search for one or more authors, type names here. If not, just press enter.')
inauthor = input()

payloadstring = "au"+": "+inauthor
print (payloadstring)

# asking for 
print('If you want to search for certain keywords in the title, input the keywords here. If not, just press enter.')
intitle = input()

payloadstring = payloadstring + ", "+"ti"+": "+intitle
print (payloadstring)

payload = {payloadstring}
print (payload)
#r = requests.get('http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?', params=payload)

#test if the url is assembled right
#print(r.url)

# asking the user of the program to choose the search type
#print('What search type do you want to use? Enter "querytext" if you want to search for keywords in documents:')
#searchtype1 = input()

# ask the user for the keywords to the search type
#print('Now type the keywords you want to search for in the database:')
#keywords1 = input()

# try to assemble the request url a little more automatically by passing parameters with params

#payload = {searchtype1: keywords1}
#r = requests.get('http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?', params=payload)

# test if the url is assembled right
#print(r.url)


# show the response to the request
#print(r.text)
