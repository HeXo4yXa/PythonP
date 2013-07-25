wrd='bubble'
y='*'
wrd1=wrd[0]
for i in range(1,len(wrd)):
    #print wrd[i]
    if wrd[i]==wrd[0]:
        wrd1+=y
    else:
        wrd1+=wrd[i]
print wrd1