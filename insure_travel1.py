from urllib import *
import re

visitedlinks=[]
rurl='insure.travel'
gurl='http://www.'+rurl

def provlink(siteurl,oldlink):
    i=0
    try:
        data_yappi = urlopen(siteurl).read()
        if '404 Page Not Found' in data_yappi:
            print '\n#######################################################'
            print 'Root: ', oldlink,'\nBad link: ',siteurl, '- 404 Page Not Found\n'
        links = re.findall("href=[\'\"](.*?)[\'\"]", data_yappi)
        for link in links:
            #print link
            if len(link)>0 and link[0]=="/":
                link=gurl+link
            #else:
            #    link='http://'+link
            if link not in visitedlinks:
                visitedlinks.append(link)
                i+=1
                print i,
                #print '\nRoot: ', oldlink, '\n','Nr:', len(visitedlinks), ' - ',link
                if rurl in link:
                    #print link
                    oldlink=siteurl
                    provlink(link,oldlink)        
    except:
        print '\n======================================================'
        print 'Root: ', oldlink, '\n','ERROR: ', siteurl, ' - ', link,'\n'

provlink(gurl,'')
print '\nTHE END',len(visitedlinks)


#print '============================================'
#provlink('http://www.yappi-club.ru/avia','')
#print '============================================'
#provlink('http://www.yappi-club.ru/avia/partners','')
#print '============================================'
#provlink('http://(http://www.yappi-club.ru/avia/partners/ukraine_international_airlines','')

#for m in re.findall(u"href='http://(.*?)'>", data_yappi):
#    print m.decode('utf-8')

#for m in re.finditer(ur"href='http://(.*?)'>(.*?)</a>", data_yappi):
#    print m.group(1)+' - '+m.group(2).decode('utf-8')