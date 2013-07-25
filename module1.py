#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      m
#
# Created:     16.03.2013
# Copyright:   (c) m 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    b=[a*a for a in range(100) if a%2]
    c=[a*a for a in range(1,101,2)]
    print (c)
    print (b)

if __name__ == '__main__':
    main()
