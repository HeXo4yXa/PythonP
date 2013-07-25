from urllib import *
import re

data_bnm = urlopen('http://www.bnm.md/en/official_exchange_rates').read()
tr1=re.compile(r'<td class="type_(number|text)">(.*)</td>')
ftr1=re.findall(tr1,data_bnm)
 
for i in range(0,len(ftr1),5):
    print '1',ftr1[i+2][1],'=', float(ftr1[i+4][1])/int(ftr1[i+3][1]),'Lei   \t ->', ftr1[i][1]