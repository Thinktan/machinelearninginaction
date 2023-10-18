import kNN

testVector = kNN.img2vector('digits/testDigits/3_10.txt')
for i in range(0, 32):
    for j in range(0, 32):
        print(int(testVector[0, i*32+j]), end='')
    print('\n', end='')