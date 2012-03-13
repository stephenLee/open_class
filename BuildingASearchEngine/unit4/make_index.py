#!/usr/bin/env python
#-*- coding: utf-8 -*-


index=[]

def add_to_index(index, keyword, url):
    for idx in index:
        if idx[0] == keyword:
            idx[1].append(url)
            return 
    # not found, add a new entry
    index.append([keyword, [url]])

def add_page_to_index(index, url, content):
	keywords = content.split()
	for keyword in keywords:
		add_to_index(index, keyword, url)

if __name__ == "__main__":
#    add_to_index(index, 'udacity', 'http://udacity.com')
 #   add_to_index(index, 'computing', 'http://acm.org')
  #  add_to_index(index, 'udacity', 'http://npr.org')
    add_page_to_index(index,'fake.text', "This is a test")
    print index
