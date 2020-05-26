def show(name):
    print(f'Przed modyfikacją: {name}')
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modyfikacji: {name}')
    print(f'ID po modyfikacji: {id(name)}')

data = ['Anna', 'Agnieszka', 'Andrzej']
print(f'Przed wywołaniem funkcji show: {data}')
print(f'ID obiektu show: {id(data)}\n')

show(data)
print(f'Po wywołaniu funkcji show {data}')

####### słownik
data1 = {0: 'Artur', 1: 'Andrzej'}
print(f'\nPrzed modyfikacją: {id(data1)}')
show(data1)

