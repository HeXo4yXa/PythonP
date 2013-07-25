from urllib import *
import re

visitedlinks=[]
rurl='insure.travel'
gurl='http://www.'+rurl
#Nr=0
def provlink(siteurl,oldlink):
    i=0
    #try:
    data_yappi = urlopen(siteurl).read()
    if 'page_under_construction' in data_yappi:
        #Nr+=1
        print '\n#######################################################'
        print 'Root: ', oldlink,'\n','Under construction: ',siteurl, '\n'
        uc=re.findall('<span style="color: #888888;">(.*?)</span>', data_yappi)
        for lnk1 in uc:
            print lnk1.decode('utf-8')        
    links = re.findall("href=[\'\"](.*?)[\'\"]", data_yappi)
    links=list(set(links))
    for link in links:
        #print 'Link#: ',link, 'Len:', len(link)
        if link[:7] != 'http://' and len(link)>0:
            if link[0] == '/':
                link=gurl+link
            else:
                link=gurl+'/'+link 
        #else:
        #    link='http://'+link
        #print 'Link: ',link
        rl=link#+oldlink
        if rl not in visitedlinks:
            visitedlinks.append(rl)
            i+=1
            print i,
            #print '\nRoot: ', oldlink, '\n','Nr:', len(visitedlinks), ' - ',link
            if rurl in link:
                #print link
                oldlink=siteurl
                provlink(link,oldlink)        
#    except:
#        print '\n======================================================'
#        print 'Root: ', oldlink, '\n','ERROR: ', siteurl, ' - ', link,'\n'

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