# -*- coding: utf-8 -*-

def primes(n):
    ''' The classical Sieve of Eratosthenes algorithm by Petropavlov Pavel
        http://py-algorithm.blogspot.com/2011/04/blog-post_09.html
        (interesting link, but only in Russian) '''
    a = [0] * n # создание массива с n количеством элементов
    for i in range(n): # заполнение массива ...
        a[i] = i # значениями от 0 до n-1
      
    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
      
    m = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n: # перебор всех элементов до заданного числа
        if a[m] != 0: # если он не равен нулю, то
            j = m * 2 # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0 # заменить на 0
                j = j + m # перейти в позицию на m больше
        m += 1
      
    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
      
    del a
    return b

def p(n):
    ''' hkapur97's solution with the Sieve of Eratosthenes '''
    m, i, l = n**0.5, 0, (n-1)//2
    a = [True] * l
    while i <= m:
        if a[i]:
            j = i + 2 * i + 3
            while j < l: a[j], j = False, j + 2 * i + 3
        i += 1
    return [2] + [2 * x + 3 for x in xrange(len(a)) if a[x]]

def p1(n):
    ''' hkapur97's solution with the Sieve of Eratosthenes.
        Modified with for loop '''
    m, i, l = n**0.5, 0, (n-1)//2
    a = [True] * l
    while i <= m:
#    for i in xrange(int(m) + 1):
        if a[i]:
            for j in xrange(i + 2 * i + 3, l, 2 * i + 3):
                a[j] = False
        i += 1
    return [2] + [2 * x + 3 for x in xrange(len(a)) if a[x]]

def p2(n):
    ''' hkapur97's solution with the Sieve of Eratosthenes.
        Modified with while loop '''
    m, i, l = n**0.5, 0, (n-1)//2
    a = [True] * l
    while i <= m:
        if a[i]:
            step = 2 * i + 3
            j = i + step
#            while j < l: a[j], j = False, j + step
            while j < l: 
                a[j] = False
                j += step
        i += 1
    return [2] + [2 * x + 3 for x in xrange(len(a)) if a[x]]

def EulerSieve33(x):
    ''' Ivan Chernikov's solution optimized by speed with Euler's Sieve ''' 
    '''p = {}
    for n in xrange(3,x+1,2):
        p[n] = True'''
    p = [True] * (x+1)
    i = 3
    sqrt_x = x**0.5
    while i <= sqrt_x:
        if p[i]:
            j = i
            prime = i * j
            while prime <= x:
                if p[prime]:
                    p[prime] = False
                j += 2
                prime = i * j
        i += 2
    return [2] + [n for n in xrange(3,x+1,2) if p[n]]

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

def Sieve2(x):
    ''' Ivan Chernikov's refined implementation of the Sieve of Eratosthenes'''
    edge = (x-1)//2
    p = [True] * edge
#    i = 0
    sqrt_edge = int((x**0.5 - 1)/2)
#    print sqrt_edge
#    while i < sqrt_edge:
    for i in xrange(sqrt_edge):
        if p[i]:
#            for j in xrange(((i + 3 + i)**2 - 3)/2, edge, i + 3 + i):
            step = i + 3 + i
            start = (step**2 - 3)/2
            for j in xrange(start, edge, step):
#                if p[j]:
                p[j] = False
#        i += 1
    return [2] + [i + 3 + i for i in xrange(edge) if p[i]]

def Sieve(n):
    ''' Modified Dustin Goodman's solution of the Sieve of Eratosthenes
        algorithm (still the fastest :-)'''
    bound = (n-1)//2
    primes = [False] * bound
    test_limit = int((n**.5 - 1) / 2) 

    for i in xrange(0, test_limit):
        if not primes[i]:
            for j in xrange(i+(3+2*i), bound, 3+2*i):
                primes[j] = True

    return [2] + [3+2*i for i in xrange(0, len(primes)) if not primes[i]]

import time

range_x = 10000000
# take a try 1,000,000 or 10,000,000 on your computer
# by the way, 100,000,000 "crashes" Ubutntu 12.04 on Intel i3 and 4GB RAM
print 'Input numbers: from 1 to', range_x 

"""t1 = time.time()
primes = primes(range_x)
t2 = time.time()
print "The Sieve of Eratosthenes by Petropavlov Pavel:"
#print primes
print '---', t2 - t1, 'sec ---', len(primes), 'primes'"""

t1 = time.time()
p = p(range_x)
t2 = time.time()
print "The Sieve of Eratosthenes by hkapur97:"
#print p
print '---', t2 - t1, 'sec ---', len(p), 'primes'

t1 = time.time()
p1 = p1(range_x)
t2 = time.time()
print "The Sieve of Eratosthenes by hkapur97 (modified with 'for'):"
#print p1
print '---', t2 - t1, 'sec ---', len(p1), 'primes'

t1 = time.time()
p2 = p2(range_x)
t2 = time.time()
print "The Sieve of Eratosthenes by hkapur97 (modified 'while'):"
#print p2
print '---', t2 - t1, 'sec ---', len(p2), 'primes'

t1 = time.time()
EulerSieve33 = EulerSieve33(range_x)
t2 = time.time()
print "Euler's Sieve by Ivan Chernikov:"
#print EulerSieve33
print '---', t2 - t1, 'sec ---', len(EulerSieve33), 'primes'

t1 = time.time()
Sieve1 = Sieve1(range_x)
t2 = time.time()
print "Derived from Euler's Sieve by Ivan Chernikov"
#print Sieve1
print '---', t2 - t1, 'sec ---', len(Sieve1), 'primes'

t1 = time.time()
Sieve2 = Sieve2(range_x)
t2 = time.time()
print "The Sieve of Eratosthenes by Ivan Chernikov (ver.2)"
#print Sieve2
print '---', t2 - t1, 'sec ---', len(Sieve2), 'primes'

t1 = time.time()
Sieve = Sieve(range_x)
t2 = time.time()
print "The Sieve of Eratosthenes by Dustin Goodman:"
#print Sieve
print '---', t2 - t1, 'sec ---', len(Sieve), 'primes'