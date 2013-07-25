def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    p1=[]
    p2=[]
    p=sorted(stones, reverse=True)
    for el in p:
        if sum(p1)>=sum(p2):
            p2.append(el)
        else:
            p1.append(el)
    return abs(sum(p1)-sum(p2))

if __name__ == '__main__':
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print 'All is ok'