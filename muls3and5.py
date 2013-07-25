#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      m
#
# Created:     17.03.2013
# Copyright:   (c) m 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

muls=[a for a in range(1,100) if (not a%3 or not a%5)]
print sum(muls)