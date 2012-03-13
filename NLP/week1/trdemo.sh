#!/usr/bin/env bash

# tr translate or delete characters

echo myfoot | tr o x
echo myfoot | tr mo Tx
echo leet | tr let 137
echo foo foo | tr " " _


echo foobar | tr [:lower:] [:upper;]
echo FooBar FOOBar | tr [:upper:] [:lower:]

echo foo | tr [a-z] x


echo foot | tr -d o
echo "   "z" "n" " | tr -d " "


echo shoooo5555hhhiHHH | tr --squeeze-repeates [a-zA-Z0-9]
echo shoooo5555hhhiHHH | tr --squeeze-repeates [:alnum:]

echo foo | tr --complement o x

