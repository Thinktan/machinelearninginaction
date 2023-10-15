
import trees, treePlotter

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lenseLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lenseTree = trees.createTree(lenses, lenseLabels)
print(lenseTree)
treePlotter.createPlot(lenseTree)