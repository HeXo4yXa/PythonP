def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    p1=[]
    p2=[]
    p=sorted(stones, reverse=True)
    if len(p)==1:
        return p[0]
    
    while len(p)>2:
        p=sorted(p, reverse=True)
        p[0]=p[0]-p[1]
        p.pop(1)
    if len(p)==2:
        p=sorted(p, reverse=True)
        return p[0]-p[1]


if __name__ == '__main__':
    print checkio([10,10])
    print checkio([10])
    print checkio([5, 8, 13, 27, 14])
    print checkio([5,5,6,5])
    print checkio([12, 30, 30, 32, 42, 49])
    print checkio([1, 1, 1, 3])
    print checkio([43,14,19,24,23,16,46])
