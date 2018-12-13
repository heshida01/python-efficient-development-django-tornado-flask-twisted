



def demoIterator():						
    print 'I am in the first call of next()'
    yield 1
    print 'I am in the second call of next()'
    yield 3
    print 'I am in the third call of next()'
    yield 9

for i in demoIterator():
    print i
