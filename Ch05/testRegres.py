from logRegres import *

dataMat, labelMat = loadDataSet()
# weights = gradAscent(dataMat, labelMat)
# plotBestFit(weights.getA())


print(len(dataMat))
# weights = stocGradAscent0(array(dataMat), labelMat)
weights = stocGradAscent1(array(dataMat), labelMat, 500)
print(weights)
plotBestFit(weights)


