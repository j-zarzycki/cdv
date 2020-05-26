print("CDV")
print(1)
'''
komentarz
blokowy
'''
#potegowanie
# = przypisane
potega= 2 ** 10
print(potega)

#pobieranie danych z klawiatury
name=input()
print("Twoje imie: " + name)
nazwisko = input()
print("Twoje imie: " + name + ", nazwisko: " + surname)
'''
Uzytkownik podaje z klawiatury swoj wiek,
Wyswietl dane w formacie: Twoj wiek: ...lat
'''
print("Podaj swoj wiek: ", end="")
age = input()
print(type(age))
print("Twoj wiek ", age)
age1=20
print(type(age1))

surname="Kowalski"
firstLetter=surname[0]
print(firstLetter)
length = len(surname)
print(length)

lastLetter=surname[len(surname)-1]
print(lastLetter)

lastLetter=surname[-1]
print(lastLetter)
