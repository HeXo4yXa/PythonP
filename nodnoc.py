def nod(x,y):
   if x!=0:
      nd=nod(y%x,x)
   else:
      nd=y
   return nd

def noc(x,y):
   nc=x*y/nod(x,y)
   return nc

y=1
for i in range(1,101):
   nc=noc(i,y)
   y=nc
   print i,"=>", nc