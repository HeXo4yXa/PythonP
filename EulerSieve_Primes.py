def Sieve1(x):
    ''' Ivan Chernikov's optimized by speed implementation with derived from
        Euler's Sieve algorithm''' 
    '''p = {}
    for n in xrange(3,x+1,2):
        p[n] = True'''
    p = [True] * (x+1)
    i = 3
    sqrt_x = x**0.5
    while i <= sqrt_x:
#    # As twice as slow with 'for i in xrange(3, sqrt_x + 1):' 
#    sqrt_x = int(x**0.5)
#    for i in xrange(3, sqrt_x + 1):
        if p[i]:
            for j in xrange(i * i, x + 1, 2 * i):
#                if p[j]:
                p[j] = False
        i += 2
    return [2] + [n for n in xrange(3,x+1,2) if p[n]]

print Sieve1(10000)