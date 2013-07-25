s=[1,3,8,120]
pq=[x*x for x in xrange(10000)]

flg=1
y=-121
while flg:
    flg=0
    for i in s:
        p=(i*y+1)
        if p not in pq:
            flg=1
            y+=1
            break
print y

