import random
l = [str(random.randint(10,99)) for i in range(101)]
#print l
f = open('test12321.txt', 'a+')
for index in l:
	f.write(index + '\n')
f.flush()
f.close()

ff= open('test12321.txt', 'r')
ll = [line.strip() for line in ff]
f.close()
print '\n',ll