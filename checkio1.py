def checkio(offers):
    '''
       the amount of money that Petr will pay for the ride
    '''
    #initial_sofi, raise_sofi, initial_oldman, reduction_oldman = offers
    initial_sofi=offers[0]
    raise_sofi=offers[1]
    initial_oldman=offers[2]
    reduction_oldman=offers[3]
    sofi=initial_sofi
    oldman=initial_oldman
    while sofi < oldman:
        if sofi >= oldman or sofi+raise_sofi >=oldman:
            return oldman
        sofi+=raise_sofi
        if sofi >= oldman or sofi >= oldman-reduction_oldman:
            return sofi    
        oldman-=reduction_oldman
        if sofi >= oldman or sofi+raise_sofi >=oldman:
            return oldman
        offers=[sofi,raise_sofi,oldman,reduction_oldman]
        checkio(offers)
    return sofi
     

if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    assert checkio([300,50,300,50]) == 300, '300'
    print 'All is ok'
    print checkio([100,150,500,100])
    
    
    