import datetime

CNP = []
mesaj = input("Introduceti CNP-ul: ")
CNP = mesaj.split()
print(CNP)

CNP_nr = ''.join(map(str, CNP))
print(CNP_nr)


# def S():
#     if CNP[0] == '1':
#         sex = print('Sex barbatesc, nascut in secolul 20')
#     elif CNP[0] == '2':
#         sex = print('Sex femeiesc, nascuta in secolul 20')
#     elif CNP[0] == '3':
#         sex = print('Sex barbatesc, nascut in secolul 19')
#     elif CNP[0] == '4':
#         sex = print('Sex femeiesc, nascuta in secolul 19')
#     elif CNP[0] == '5':
#         sex = print('Sex barbatesc, nascut in secolul 21')
#     elif CNP[0] == '6':
#         sex = print('Sex femeiesc, nascuta in secolul 21')
#     elif CNP[0] == '7':
#         sex = print('Sex barbatesc, persoana straina rezidenta in Romania')
#     elif CNP[0] == '8':
#         sex = print('Sex femeiesc, persoana straina rezidenta in Romania')
#     elif CNP[0] == '9':
#         sex = print('Persoana straina')
#     return sex


def AA(CNP_nr):
    secole = {
        '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000,
    }
    year = int(CNP_nr[1:3]) + secole.get(CNP_nr[0], 1900)
    print(year)
    month = int(CNP_nr[3:5])
    print(month)
    day = int(CNP_nr[5:7])
    print(day)
    try:
        return datetime.date(year, month, day)
    except ValueError:
        return False #Data invalida



def JJ(CNP_nr):
    cod_judet = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                 '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                 '41', '42', '43', '44', '45', '46', '51', '52'
    }
    while CNP_nr[7:9] in cod_judet:
        return True #Judet valid
    else:
        return False #Judet invalid



def NNN(CNP_nr):
    n1 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    n2 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    n3 = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    while CNP_nr[9] in n1 and CNP_nr[10] in n2 and CNP_nr[11] in n3:
        return True #NNN valid
    else:
        return False #NNN invalid



def C(CNP_nr):
    control = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
    check = sum(w * int(n) for w, n in zip(control, CNP_nr)) % 11
    print(check)
    return '1' if check == 10 else str(check)



def validare_cnp(CNP_nr):
    while len(CNP_nr) != 13:
        print("CNP invalid")
    if CNP_nr[0] not in '123456789':
        print("Sex invalid")
    if AA(CNP_nr) is False:
        print("Data invalida")
    elif JJ(CNP_nr) is False:
        print("Judet invalid")
    elif NNN(CNP_nr) is False:
        print("NNN invalid")
    elif C(CNP_nr[:-1]) != CNP_nr[-1]:
        print("Cifra de control invalida")
    else:
        print("CNP valid")

validare_cnp(CNP_nr)
