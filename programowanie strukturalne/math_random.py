#pi
import math
pi=math.pi
print(pi)

#pierwiastek
x=math.sqrt(9)
print(x)

#losowanie
import random
rand=random.random()
print(rand)

list=random.choice([1, 2, 3, 4, 5, 6])
print(list)

number = int(input("Podaj liczbę całkowitą od 1 do 10\n"))
if(number <= 10):
    print(number)
    number=random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print('Porównanie wylosowanej liczby z tą podaną przez użytkownika')
    print(number)
    print('Gratulacje')
if(number > 10):
    print('Spróbuj innym razem')
if (number < 0):
    print('Spróbuj innym razem')