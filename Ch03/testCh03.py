import trees
import treePlotter

myDat, labels = trees.createDataSet()
myTree = treePlotter.retrieveTree(0)
print('labes:', labels)
print('myTree:', myTree)

trees.storeTree(myTree, 'classifirerStorage.txt')
myRecTree = trees.grabTree('classifirerStorage.txt')

print('answer1:', trees.classify(myTree, labels, [1, 0]))
print('answer2:', trees.classify(myRecTree, labels, [1, 0]))