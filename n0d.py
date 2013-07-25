def prb (a):
    x=a
    fl=1
    while fl:
        fl=0
        for i in range(a,1,-1):
            if x%i:
                fl=1
                x+=1
                break
    return x

for x in range(2,18):
    print x, "=>",prb(x)