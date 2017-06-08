mx = lambda x, y: x if x > y else y
print(mx(100, 8))

n = [1, 2, 3, 4]
nx = list(map(lambda z: z**2, n))
print(nx)

m = [8, 7, 1, 9, 3]
dx = list(filter(lambda k: k > 2, m))
print(dx)

t = [2, 7, 9, 3]
from functools import reduce
kx = reduce(lambda a,b:a*b,t)
print(kx)
