from urllib import *
import re
visitedlinks=[]

def provlink(siteurl):
    i=0
    try:
        data_yappi = urlopen(siteurl).read()
        if '404 Page Not Found' in data_yappi:
            print '\n----------------------------------------\n'
            print siteurl, '- 404 Page Not Found\n'
    except:
        print "ERROR: ", siteurl
    links = re.findall("=[\'\"]http://(.*?)[\'\"]", data_yappi)
    for link in links:
        #print link
        link='http://'+link
        if link not in visitedlinks:
            visitedlinks.append(link)
            #i+=1
            #print i,
            print 'Nr:', len(visitedlinks), ' - ',link
            if 'insure.travel' in link:
                #print link
                provlink(link)

provlink('http://insure.travel/')
#print '============================================'
#provlink('http://www.yappi-club.ru/avia')
#print '============================================'
#provlink('http://www.yappi-club.ru/avia/partners')
#print '============================================'

#for m in re.findall(u"href='http://(.*?)'>", data_yappi):
#    print m.decode('utf-8')

#for m in re.finditer(ur"href='http://(.*?)'>(.*?)</a>", data_yappi):
#    print m.group(1)+' - '+m.group(2).decode('utf-8')