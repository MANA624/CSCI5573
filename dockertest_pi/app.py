import sys
import numpy as np

np.random.seed(int(sys.argv[1]))

for i in range(10000):
    a = np.random.rand(100,1)
    b = np.random.rand(100,1)
    c = np.dot(b, a.T)
    d = np.matrix.sort(c)

print(int(np.sum(c)))