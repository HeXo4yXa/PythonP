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
    if sofi >= oldman:
        return oldman
    else: sofi+=raise_sofi
    if sofi >= oldman or sofi >= oldman-reduction_oldman:
        return sofi
    else: oldman-=reduction_oldman
    if sofi >= oldman or sofi+raise_sofi >=oldman:
        return oldman
    else:
        offers=[sofi,raise_sofi,oldman,reduction_oldman]
        checkio(offers)


if __name__ == '__main__':
    print checkio([130,10,170,10])