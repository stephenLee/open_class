
#Define a function, hash_string,
#that takes as inputs a keyword
#(string) and a number of buckets,
#and outputs a number representing
#the bucket for that keyword.

#print hash_string('a',12) => 1
#print hash_string('b',12) => 2
#print hash_string('a',13) => 6

#print hash_string('au',12) => 10
#print hash_string('udacity',12) => 11

def hash_string(keyword, buckets):
    h = 0
    for c in keyword:
        # for long keyword, this can reduce computing numbers.
        h = (h + ord(c)) % buckets 
    return h

#Creating an Empty Hash Table
#Define a procedure, make_hashtable,
#that takes as input a number, nbuckets,
#and outputs an empty hash table with
#nbuckets empty buckets.
###############
# [[]] * 3 why wrong, the three list reference the same empty list
################
def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table

#Define a procedure, hashtable_get_bucket,
#that takes two inputs - a hashtable, and
#a keyword, and outputs the bucket where the
#keyword could occur.

#hash_string(keyword,nbuckets) => index of bucket

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]


#Define a procedure,

#hashtable_add(htable,key,value)

#that adds the key to the hashtable
#(in the correct bucket), with the
#correct value.

def hashtable_add(htable,key,value):
    
