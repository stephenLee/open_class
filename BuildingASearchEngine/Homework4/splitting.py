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
    output = []
    atsplit = True  # At a split point
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                # add character to last word
                output[-1] = output[-1] + char
    return output

if __name__ == "__main__":
    out = split_string("This is a test-of the,string separation-code!", " ,!-")
    print out
