import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 0], 15.0*array(datingLabels), 15.0*array(datingLabels))
# plt.show()

dataSet = datingDataMat
minVals = dataSet.min(0)
maxVals = dataSet.max(0)

# print('minVals:', minVals)
# print('maxVals:', maxVals)
ranges = maxVals - minVals
# print('ranges: ', ranges)
# print('shape(dataSet): ', shape(dataSet))
normDataSet = zeros(shape(dataSet))
m = dataSet.shape[0]
# print('m: ', m)
# print('shape(tile(minVals, (m, 1))): ', shape(tile(minVals, (m, 1))))
normDataSet = dataSet - tile(minVals, (m, 1))
normDataSet = normDataSet / tile(ranges, (m, 1))  # element wise divide
print(normDataSet)
print(ranges)
print(minVals)
print('------')
normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
print(normMat)
print(ranges)
print(minVals)