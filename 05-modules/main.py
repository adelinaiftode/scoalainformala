# print() #str
# input() #str
# "".format() #str

# def functie2():
#    my_function()

# def my_function():
#   function body
#    return 'None'
#    pass
# print(functie2())

# def your_function(x: str) -> str:
#    return f"Hello, {x}"
#
# name = input("Numele meu este: ")
# your_function(name)

# def my_function(a: str, b: str, c: str = '2') -> (str, str, str):
#     return a, b, c

# print(my_function(a='1', c='2', b='3'))
# print(my_function('1', '3', '2'))
# print(my_function('1', c='2', b='3'))
# print(my_function('3', a='2', c='3')) #eroare
# print(my_function('1', '3', c='2', d='4')) #eroare
# print(my_function('1', '3', '4'))

# def my_function():
#     pass

# a = my_function()
# print(a)
# b = None
# print(type(b))

#def my_function(n: int) -> bool:
#    if n % 2 ==0:
#        return True
#    return False


#print(my_function(3))
#nr = input("Introdu un numar: ")
#if my_function(int(nr)) is True:
#    print("Numarul este divizibil")
#elif my_function(int(nr)) is False:
#    print("Numarul nu este divizibil")

#
# def my_function(var1):
#     global var
#     var = var1
#     return f"Cunosti aceasta variabila: {var}"
#
#
# print(my_function(3))
# var = 1
# print(var)

# lista = [1, 2, 3, [4, 5, [6, 7]]]
# print(lista[3][2][0])

# try:
#     # bloc de expresii
# except:
#     #daca apare o exceptie

try:
    valoare = int(input("Prima cifra din CNP: "))
    # impartire = 1/valoare
    lista = [1]
    # # lista.append("2")
    # valoare = lista[0.5]
    print("Sunt in try")
except (TypeError, AttributeError, ValueError, ZeroDivisionError):
    print("Tip de eroare")
else:
    print("Nu exista exceptie")
finally:
    print("Se executa oricum")
print("Am iesit din try-except")
# except AttributeError:
#     print("Eroare la atribuire")
# except ValueError:
#     print("Ai introdus o litera in loc de cifra")
# except Exception as e:
#     print("Exceptie la imparire", e)
# except ZeroDivisionError:
#     print("Eroare la impartire")
# except Exception as e:
#     print("Exceptie la imparire", e)