from math import sqrt, pow

print(sqrt(25))

import math as m
print(m.pow(2,4))

import random as r
rand = r.random()
print(rand)

randOfList = r.choice([1, 2, 3 ,4])
print(randOfList)

print(r.randrange(10, 20))
print(r.randrange(10))
print(r.randrange(9, 13, 2))

###

numList = [10, 20, 30, 40, 45]
numTuple = (1, 2, 3, 4, 5)
text = 'janusz'

print('Lista: ' + str(r.choice(numList)))
print('Tuple: ' + str(r.choice(numTuple)))
print('Text: ' + str(r.choice(text)))

###

print()
print(numList)
r.shuffle(numList)
print(numList)
