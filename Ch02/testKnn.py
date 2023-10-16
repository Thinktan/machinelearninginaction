import kNN

inX = [0, 0]
group, labels = kNN.createDataSet()
print(kNN.classify0(inX, group, labels, 3))
