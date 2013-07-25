n=5
nn=0
for nm in xrange(10**(n-1)-1,10**n):
    nm=list(str(nm))
    p=1
    s=0
    for c in nm:
        p*=int(c)
        s+=int(c)
    if p==s:
        nn+=1
print nn