m=543210 # chislitel'
n=12345 # znamenatel'
k=5300 # chisel posle zapyatoy
ni=m/n
nm=m*10**k/n
if len(str(nm)) < k:
    fnm=str(ni)+'.'+('0'*(k-len(str(nm))))+str(nm)
else:
    fnm=str(ni)+'.'+str(nm).replace(str(ni),'',1 )

print 'fnm=', fnm