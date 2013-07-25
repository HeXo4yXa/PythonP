def prb (a=2,b=2):
    x=a
    fl=1
    while fl:
        fl=0
        for i in range(b,1,-1):
            if x%i:
                fl=1
                x+=1
                break
    print b,"=>",x
    prb(x*2-1,b+1)




prb()
