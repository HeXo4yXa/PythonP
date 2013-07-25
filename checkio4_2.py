def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''

    s1=[]
    s1.extend(stones)
    s2=[]
    minv=sum(s1)
    n=2**len(stones)
    if len(stones)==1:
        return sum(stones)
    if len(stones)==2:
        return abs(stones[0]-stones[1])
    if len (stones)>2:
        for i in xrange(1,n-1):
            for j in xrange(len(stones)):
                if (i & (1 << j)):
                    #print stones[j]
                    s2.append(stones[j])
                    s1.remove(stones[j])
            
            sum_s= abs(sum(s2)-sum(s1))
            if minv > sum_s:
                minv = sum_s
                #print s2,' --- ',s1
                #print minv, '\n'
            s2=[]
            s1=[]
            s1.extend(stones)
        return minv

if __name__ == '__main__':
    print checkio([10,10])
    print checkio([10])
    print checkio([5, 8, 13, 27, 14])
    print checkio([5,5,6,5])
    print checkio([12, 30, 30, 32, 42, 49])
    print checkio([1, 1, 1, 3])
    print checkio([43,14,19,24,23,16,46])
