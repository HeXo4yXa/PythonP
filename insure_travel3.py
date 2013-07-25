from urllib import *
import re

visitedlinks=[]
rurl='insure.travel'
gurl='http://www.'+rurl

def provlink(siteurl,oldlink):
    i=0
    #try:
    data_yappi = urlopen(siteurl).read()
    if '404 Page Not Found' in data_yappi:
        print '\n#######################################################'
        print 'Root: ', oldlink,'\nBad link: ',siteurl, '- 404 Page Not Found\n'
    links = re.findall("href=[\'\"](.*?)[\'\"]", data_yappi)
    links=list(set(links))
    for link in links:
        #print 'Link#: ',link, 'Len:', len(link)
        if link[:7] != 'http://' and len(link)>0:
            if link[0] == '/':
                link=gurl+link
            else:
                link=gurl+'/'+link 
                
        print link

provlink(gurl,'')
print '\nTHE END',len(visitedlinks)