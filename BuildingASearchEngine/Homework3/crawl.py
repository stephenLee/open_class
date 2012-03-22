#!/usr/bin/env python
#-*- coding: utf-8 -*-


#The web crawler we built at the
#end of Unit 2 has some serious
#flaws if we were going to use
#it in a real crawler. One
#problem is if we start with
#a good seed page, it might
#run for an extremely long
#time (even forever, since the
#number of URLS on the web is not
#actually finite). The final two
#questions of the homework ask
#you to explore two different ways
#to limit the pages that it can
#crawl.


#######


#Modify the crawl_web procedure
#to take a second parameter,
#max_pages, that limits the
#number of pages to crawl.
#Your procedure should
#terminate the crawl after
#max_pages different pages
#have been crawled, or when
#there are no more pages to crawl.



#The following definition of
#get_page provides an interface
#to the website found at
#http://www.udacity.com/cs101x/index.html

#The function output order does not affect grading.

#crawl_web("http://www.udacity.com/cs101x/index.html",1) => ['http://www.udacity.com/cs101x/index.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",3) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",500) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html', 'http://www.udacity.com/cs101x/crawling.html', 'http://www.udacity.com/cs101x/kicking.html']


import urllib

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

#The web crawler we built at the
#end of Unit 2 has some serious
#flaws if we were going to use
#it in a real crawler. One
#problem is if we start with
#a good seed page, it might
#run for an extremely long
#time (even forever, since the
#number of URLS on the web is not
#actually finite). The final two
#questions of the homework ask
#you to explore two different ways
#to limit the pages that it can
#crawl.


#######

#TWO GOLD STARS#

#Modify the crawl_web procedure
#to take a second parameter,
#max_depth, that limits the
#minimum number of consecutive
#links that would need to be followed
#from the seed page to reach this
#page. For example, if max_depth
#is 0, the only page that should
#be crawled is the seed page.
#If max_depth is 1, the pages
#that should be crawled are the
#seed page and every page that links
#to it directly. If max_depth is 2,
#the crawl should also include all pages
#that are linked to by these pages.


#The following definition of
#get_page provides an interface
#to the website found at
#http://www.udacity.com/cs101x/index.html

#The function output order does not affect grading.

#crawl_web("http://www.udacity.com/cs101x/index.html",0) => ['http://www.udacity.com/cs101x/index.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",1) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html', 'http://www.udacity.com/cs101x/crawling.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",50) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html', 'http://www.udacity.com/cs101x/crawling.html', 'http://www.udacity.com/cs101x/kicking.html']

def crawl_web(seed, max_depth):
    tocrawl = [[seed,0]]
    crawled = []
    while tocrawl:
        page, depth = tocrawl.pop()
        if page not in crawled and depth <= max_depth:
            for link in get_all_links(get_page(page)):
                tocrawl.append([link, depth+1])
            crawled.append(page)
    return crawled

def crawl_web1(seed, max_pages):
    tocrawl = [seed]
    crawled = [] # len(crawled) is length of crawled
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

if __name__ == "__main__":
    result1 = crawl_web("http://www.udacity.com/cs101x/index.html", 1)
    result2 = crawl_web("http://www.udacity.com/cs101x/index.html", 3)
    result3 = crawl_web("http://www.udacity.com/cs101x/index.html", 500)
    result4 = crawl_web1("http://www.udacity.com/cs101x/index.html", 1)
    result5 = crawl_web1("http://www.udacity.com/cs101x/index.html", 3)
    result6 = crawl_web1("http://www.udacity.com/cs101x/index.html", 500)
    print result1 
    print result2 
    print result3 
    print result4
    print result5
    print result6
