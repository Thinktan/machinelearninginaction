import bayes

listOfPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOfPosts)
print(myVocabList)

trainMat = []
for postinDoc in listOfPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))

# print(trainMat)
p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)

# print('p0V: ', p0V)
# print('p1V: ', p1V)
# print('pAb: ', pAb)
# print(myVocabList[p1V.argmax()])

bayes.testingNB()