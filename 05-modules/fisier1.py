# # import primul_nostru_modul
# # from primul_nostru_modul import my_sum as suma
# from Functions04.calculator import suma
#
# # import math
# # from math import fsum
#
#
# if __name__ == '__main__':
#     print(suma(4, 5), __name__)
#     #print(primul_nostru_modul.my_sum(1, 4))

my_var = input("Numar intreg: ")
my_int = None
try:
    my_int = my_var
except Exception as e:
    print("Exceptie generica", e, my_int)
    my_int = 'test'
else:
    print("Daca nu apare exceptie ", my_int)
finally:
    my_int = 'www'
    print("Afiseaza in orice caz", my_int)
print(my_int)
