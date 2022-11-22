import random
import time

VALORMINIMOPARA_XYZW = 0
VALORMAXIMOPARA_XYZW = 10
QUANTIDADE_POPULACAO = 10


# for n in range(0,11):
#     numero = format(n,'b')
#     while numero.__len__() < 4:
#         numero = '0'+numero
#     print('if n == {}:\n\treturn \'{}\'\nel'.format(n,numero),end='')

def printer(l: list):
    for x in l:
        print(x)


def toBin(n):
    if n == 0:
        return '0000'
    elif n == 1:
        return '0001'
    elif n == 2:
        return '0010'
    elif n == 3:
        return '0011'
    elif n == 4:
        return '0100'
    elif n == 5:
        return '0101'
    elif n == 6:
        return '0110'
    elif n == 7:
        return '0111'
    elif n == 8:
        return '1000'
    elif n == 9:
        return '1001'
    elif n == 10:
        return '1010'


def funcaoFitness(x, y, z, w):
    return 5 * x + y * 2 + w + z * 3


def rnd():
    return random.randint(VALORMINIMOPARA_XYZW, VALORMAXIMOPARA_XYZW)

def cria():
    x = rnd()
    y = rnd()
    z = rnd()
    w = rnd()
    cc = '{}{}{}{}'.format(toBin(x), toBin(y), toBin(z), toBin(w))
    ft = funcaoFitness(x, y, z, w)
    return [x, y, z, w, cc, ft]


def cria_populacao_inicial(numero=QUANTIDADE_POPULACAO):
    lista = []

    for n in range(0, numero):
        lista.append(cria())
    f = open('populacaoInicial.txt', 'w')
    f.write(lista.__str__())
    f.close()
    return sorted(lista, key=lambda w: w[5], reverse=True)


populacaoInicial = cria_populacao_inicial()
printer(populacaoInicial)