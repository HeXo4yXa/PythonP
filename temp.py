infile=open("INPUT.TXT")
outfile=open("OUTPUT.TXT","w")

dt=[int(x) for x in infile.readline().split()]
#print (dt)
s=dt[0]*dt[1]
#print (s)
squares=int(infile.readline())

sq=0
ssqa=0
while sq<int(squares):
    dta=[int(x) for x in infile.readline().split()]
    sqa=(int(dta[2])-int(dta[0]))*(int(dta[3])-int(dta[1]))
    sq+=1
    ssqa+=sqa
outfile.write(str(s-ssqa))
infile.close()
outfile.close()
    
