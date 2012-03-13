#!/usr/bin/env python
#-*- coding: utf-8 -*-

index = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing',['http://acom.org']]]

def look_up(index, keyword):
    for idx in index:
        if idx[0] == keyword:
            return idx[1]
    return []

if __name__ == '__main__':
    print look_up(index, 'udacity')
    print look_up(index, 'hello')
