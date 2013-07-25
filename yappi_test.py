from urllib import *
import re
visitedlinks=[]

def provlink(siteurl):
    data_yappi = urlopen(siteurl).read()
    if '404 Page Not Found' in data_yappi:
        print '\n ---------------------------------------- \n'
        print siteurl, '- 404 page not Found\n'
    links = re.findall("<a href='(.*?)'", data_yappi)
    for link in links:
        #print link
        if link not in visitedlinks:
            print link, ' - Not visited Nr:', len(visitedlinks)
            visitedlinks.append(link)
            if 'yappi-club.ru' in link:
                provlink(link)
        else:
            print link, ' - Visited' 


provlink('http://www.yappi-club.ru')
print '============================================'
#provlink('http://www.yappi-club.ru/avia')
#print '============================================'
#provlink('http://www.yappi-club.ru/avia/partners')
#print '============================================'

#for m in re.findall(u"href='http://(.*?)'>", data_yappi):
#    print m.decode('utf-8')

#for m in re.finditer(ur"href='http://(.*?)'>(.*?)</a>", data_yappi):
#    print m.group(1)+' - '+m.group(2).decode('utf-8')