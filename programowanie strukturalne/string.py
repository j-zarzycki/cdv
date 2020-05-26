text = "Anna, pawel, tomek"

'''
komentarz
blokowy
'''
tab=text.split(", ")
print(text)
print(tab)
print(type(tab))
name1=tab[0]
print("Twoje imie: ", name1)

nameUpper=name1.upper()
print(nameUpper)

nameLower=name1.lower()
print(nameLower)

#sprawdzanie zawartosci
surname=input()
content=surname.isalpha()
print(content)
name="Katarzyna"
print("\nDane uzytkownika: \nMasz na imie: ", name)

text1="Jan\n"
text2="Nowak"
print(text1 + text2)
text=text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#wyswietlanie lancuchów znakow

text = "%s, Java i %s" % ("PHP","Python")
print(text)
text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)
new=text.replace("PHP", "C#")
print(new)
#wypisanie danych
year=2020 #przypisz 2020
month="may"
day=5

print("Data: ", end-"")
print(day, month, year)

print(day, month, year, sep="-")
