#listy
progr=['PHP', 'Python']
print(progr)
progr.append('C#')
print(progr)
count=progr.count('PHP')
print(f'PHP występuje {count} razy\n')

#tuple
name=('Krystyna', 'Tomasz')
print(name)
print(type(name))
first=name[0]
print(first)
#name.append('Janusz') nie mozna dodawac nowych elementow
#ale przez to tuple sa szybsze

#słowniki
person = {
    'name' : 'Anna'
}
print(person)
print(type(person))
print(person['name'])
print(person.keys())
person['weight'] = 75
print(person.get('weight', 'brak danych'))

#zadanie
n1 = input("\nPodaj pierwsze imię:")
n2 = input("Podaj drugie imię:")
n3 = input("Podaj trzecie imię:")

name = {
  0:n1,
  1:n2,
  2:n3
}

for key, value in name.items():
  count=key+1
  print(f'Imię{count}:{value}')

'''
print(f'Imię1: {name[0]}')
print(f'Imię2: {name[1]}')
print(f'Imię3: {name[2]}')
'''