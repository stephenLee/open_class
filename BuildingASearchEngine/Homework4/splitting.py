#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Define a procedure, split_string, that takes two
#inputs: the string to split and a string containing
#all of the characters considered separators.

#out = split_string("This is a test-of the,string separation-code!", " ,!-")
#print out => ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out."," .")
#print out => ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

def split_string(source, splitlist):
    out = source
    for sep in splitlist:
        out = out.split(sep)
    return out

if __name__ == "__main__":
    out = split_string("This is a test-of the,string separation-code!", " ,!-")
    print out
