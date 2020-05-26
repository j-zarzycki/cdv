dict={'key1':'value1', 'key2':'value2'}

worker = {
    'name' : 'Anna',
    'surname' : 'Nowak',
    'city' : 'Poznań',
    'age' : 20,
    'childrenNames' : ['Tomasz', 'Krystyna'],
    'parentsNames' : ['Paweł', 'Katarzyna'],
}

print(worker)
print(worker['childrenNames'])
print('Dziecko1: ' + str(worker['childrenNames'][0]))
print('Dziecko2: ' + str(worker['childrenNames'][1]))

worker['height']=180
worker['weight']=80
print(worker)

key='age'
if key in worker:
    del worker[key]
    print(f'klucz o nazwie {key} został usunięty')
else:
    print(f'Klucz o nazwie {key} nie znaleziono w słowniku worker')
    print(worker)
    print(worker.values())
    print(worker.items())

    pracownik = {
        'name': 'Anna',
        'surname': 'Nowak',
        'city': 'Poznań',
        'age': 20,
        'childrenNames': ['Tomasz', 'Krystyna'],
        'parentsNames': ['Paweł', 'Katarzyna'],
    }

    for value in worker.values():
        print(value, end=' ')

        print(pracownik)
        print(pracownik.values())
        print(pracownik.items())

        for value in pracownik.values():
            print(value, end=" ")