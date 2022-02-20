# Să se scrie o funcție care primește un număr nedefinit de parametri
# și să se calculeze suma parametrilor care reprezintă numere întregi sau reale

def suma_int_real(*arr1, **arr2):
    return sum(filter(lambda i: isinstance(i, int), arr1))


print(suma_int_real(1, 5, -3, 'abc', [12, 56, 'cad']))
print(suma_int_real())
print(suma_int_real(2, 4, 'abc', param_1=2))

# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# suma tuturor numerelor de la [0, n]
# suma numerelor pare de la [0, n]
# suma numerelor impare de la [0. n]


def suma(n):
    if n == 0:
        return 0

    return n + suma(n-1)


def suma_elem_pare(n):
    if n == 0:
        return 0
    if not n % 2 == 0:
        return suma_elem_pare(n-1)
    else:
        return n + suma_elem_pare(n-1)


def suma_elem_impare(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return suma_elem_impare(n-1)
    else:
        return n + suma_elem_impare(n-1)


numar = int(input("Alege un numar intreg: "))
print(suma(numar))
print(suma_elem_pare(numar))
print(suma_elem_impare(numar))


# Să se scrie o funcție care citește de la tastatură și
# returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0


def numar_intreg(x):
    if x.isnumeric():
        return x
    else:
        return 0


nr = input("Introduceti numarul: ")
print(numar_intreg(nr))
