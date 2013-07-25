import random
b=[a*a for a in range(100) if a%2]
print (b)
c=filter(lambda x: x%2,[random.randint(-100, 100) for a in range(100)])
print (c)
