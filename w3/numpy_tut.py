__author__ = 'baio'

print "Importing numpy"

import numpy as np

print "Createing matrixes"

zeroArray = np.zeros((2, 3))
print zeroArray

oneArray = np.ones((2, 3))
print oneArray

emptyArray = np.empty((2, 3))
print emptyArray

randomArray = np.random.random((2, 3))
print randomArray

foo = [[1, 2, 3], [4, 5, 6]]
myArray = np.array(foo)
print myArray

# reshape arrays
rg = np.arange(6, 12)
print rg

rg = rg.reshape((3, 2))

print rg.reshape((3, 2))

print rg[0, 0]

sq = np.arange(1, 10).reshape((3, 3))
print(sq)


print rg[0, 0:2]

print sq
print sq[0:2, 1:3]

print sq[:, 0:3:2]

sq[0, :] = np.array(range(5, 8))
#sq[1, 0] = 77
print sq


idx = np.array([1, 1, 2, 3])
rnd = np.random.random((10, 1))
print rnd
print rnd[idx]

bidx = np.array([[True, False, False], [True, False, False], [True, False, False]])
print sq[bidx]

brows = np.array([False, True, False])
bcols = np.array([True, False, True])

#print sq[brows, bcols]

avg = np.average(sq)
print avg
better = sq > avg
print better
print sq[better]


std = np.std(sq)

clamped = np.array(sq.copy(), dtype=float)
clamped[(sq - avg) > std] = avg + std
clamped[(sq - avg) < -std] = avg - std
print clamped

print sq * 2

print sq + np.ones((3, 3))

print sq * np.arange(1,10).reshape((3,3))

mata = np.array([[1, 2], [3, 4]])
matb = np.array([[5, 6], [7, 8]])

print np.dot(mata, matb)