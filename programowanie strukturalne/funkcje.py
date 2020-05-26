def witaj():
    print('Witaj ', end='')
    print('Janusz')

    witaj()

    def showAge(age):
        print(f'Masz na imię: {age}')
        showAge(23)

        def iloczyn(a, b):
            return a * b
        print(iloczyn(3, 4))

        def iloraz(a, b):
            return a / b
        print(iloraz(7, 3))
        print(iloraz(b=7, a=3))
