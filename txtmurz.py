# -*- coding: utf-8 -*-
import string
i=0
txt=open("txt.txt")
punc="!@#$%^&*()_+=-<>?,./\\|\"\':;~"
for string1 in txt:
    i+=string1.upper().translate(None, punc).split().count('THE')
    print (string1.upper().translate(None, punc).split())
    print (i)