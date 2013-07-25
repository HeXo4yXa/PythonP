'''
x**y-y**x=0
x=y**2
'''

for y in range(100):
    x=y*y
    if x**y==y**x:
        print x,'^',y,'-',y,'^',x,'=0'