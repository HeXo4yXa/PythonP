'''
122333444455555666666 
'''
s=''
i=1
while len(s)<1000:
    s+=''.join(str(i)*i)
    i+=1
print s,'\n',i-1
