import numpy
array = numpy.random.randint(0,10, size=(5,5), dtype=int)
print(array)
print(array[2,3])
# I don't know if you wanted to include the 0th column/row as the first or not
print(numpy.sum(array))
print(numpy.mean(array,axis=1))
print(numpy.max(array,axis=0))