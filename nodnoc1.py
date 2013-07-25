def nod(x,y): return x if y == 0 else nod(y, x % y)
def noc(x,y): return (x/nod(x,y))*y

nc=1
for i in range(1,1334):
   nc=noc(i,nc)
   print i,"=>", nc