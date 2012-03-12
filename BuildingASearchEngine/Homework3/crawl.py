#!/usr/bin/env python
#-*- coding: utf-8 -*-

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

def crawl_web(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    depth = 1
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
        depth += 1

    return crawled

def crawl_web1(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl and (len(crawled) < max_pages):
        page = tocrawl.pop()
        if page not in crawled:
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
