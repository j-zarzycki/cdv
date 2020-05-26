programowanie=['Python', 'PHP', 'C#', 'JS', 'JAVA']
print(programowanie)
print(type(programowanie))
first=programowanie[0]
print("Pierwszy element: ", first)
threeElements=programowanie[0:3]
print(threeElements)
lastElements=programowanie[-1]
print(lastElements)

#dodanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#zliczanie elementu w liście
countElements=programowanie.count("Python")
print(countElements)

#ilość elementów w liście
countElementsOfList=len(programowanie)
print("Ilość elementów w liście: " + str(countElementsOfList))

#połączenie list
anotherList=['C', 'C++']
programowanie.extend(anotherList)
print("Lista programowanie: " + str(programowanie))
print("Lista anotherList: " + str(programowanie))

#usuwanie elementó listy
new=programowanie
print("New list: " + str(new))
new.clear()
print("New list: " + str(new))
print("Rozmiar new list: " + str(len(new)))
print("Programowanie: " + str(programowanie))
print("Rozmiar listy programowanie: " + str(len(programowanie)))
x=8
print(x)
y=x

print(y)

y=5
print(x)
print(y)
