from logRegres import *

dataMat, labelMat = loadDataSet()
# weights = gradAscent(dataMat, labelMat)
# plotBestFit(weights.getA())


print(len(dataMat))
weights = stocGradAscent0(array(dataMat), labelMat)
print(weights)
# plotBestFit(weights)


