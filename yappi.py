from urllib import *
import re

data_yappi = urlopen('http://www.yappi-club.ru/avia/partners').read()
#tr1=re.compile(r"href='http://(.*)</a>")
#ftr1=re.findall(tr1,data_yappi)
#print ftr1

for m in re.findall('=[\'\"]http://(.*?)[\'\"]', data_yappi):
    print m#.decode('utf-8')
    
    
#for m in re.finditer(ur"href='http://(.*?)'>(.*?)</a>", data_yappi):
#    print m.group(1)+' - '+m.group(2).decode('utf-8')