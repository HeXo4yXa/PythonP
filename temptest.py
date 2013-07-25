from urllib import *
import re

visitedlinks=[]
rurl='insure.travel/apply'
gurl='http://www.'+rurl
#Nr=0
def provlink(siteurl,oldlink):
    i=0
    #try:
    data_yappi = urlopen(siteurl).read()
    print data_yappi
    print '\n#######################################################'
    print 'Root: ', oldlink,'\n','Under construction: ',siteurl, '\n'
#    uc=re.findall('<span style="color: #888888;">(.*?)</span>', data_yappi)
#    for lnk1 in uc:
#        print lnk1.decode('utf-8')

provlink(gurl,'')
print '\nTHE END',len(visitedlinks)