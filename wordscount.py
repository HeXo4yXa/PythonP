txt=open("txt.txt")

ft={}
for line in txt:
    for word in line.upper().split():
        if not word in ft.keys():
            ft[word]=1
        else:
            ft[word]+=1
#print ft, '\n'

i=0
for key, value in sorted(ft.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    if i < 20:
        print "%s: %s" % (key, value)
        i+=1