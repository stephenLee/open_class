#！/usr/bin/env python

#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1
"""
def edit_distance(s,t):
    if len(s) < len(t):
        return levenshtein(t, s)
    if not s:
        return len(t)
    
    previous_row = xrange(len(t) + 1)
    for i, c1 in enumerate(s):
        current_row = [i + 1]
        for j, c2 in enumerate(t):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]


"""
def edit_distance(s,t):
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)
    if s[0] == t[0]:
        return edit_distance(s[1:], t[1:])
    else:
        return min(1 + edit_distance(s[1:], t[1:]),
                   1 + edit_distance(s, t[1:]),
                   1 + edit_distance(s[1:], t))
#For example:

# Delete the 'a'
#print edit_distance('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
#print edit_distance('audacity', 'Udacity')
#>>> 2

# Five replacements
#print edit_distance('peter', 'sarah')
#>>> 5

# One deletion
#print edit_distance('pete', 'peter')
#>>> 1
