def checkio(data):
    'Return True if password strong and False if not'
    passwd=data
    print passwd
    print 'len', len(passwd), len(passwd)>9
    print 'alpha', passwd.isalpha()
    print 'digit', passwd.isdigit()
    print 'lower', passwd.islower()
    print 'upper', passwd.isupper()
    return (len(passwd)>9 and not passwd.isalpha() and not passwd.isdigit() and not passwd.islower() and not passwd.isupper())
if __name__ == '__main__':
    checkio('A1213pokl')
    checkio('bAse730onE4')
    checkio('asasasasasasasaas')
    checkio('QWERTYqwerty')
    checkio('123456123456')
    checkio('QwErTy911poqqqq')
    checkio('QWERTY911POQQQQQQ')