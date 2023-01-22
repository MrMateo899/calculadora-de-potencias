bas = int(input('Inserte la base: '))
exp = int(input('Inserte el exponente: '))

if exp > 3:
    print(f'{bas} elevado a {exp} es igual a:', bas**exp)
elif exp == 2:
    print(f'{bas} al cuadrado es igual a:', bas**2)
elif exp == 3:
    print(f'{bas} al cubo es igual a:', bas**3)