import random
import time

VALORMINIMOPARA_XYZW = 0
VALORMAXIMOPARA_XYZW = 10
VALORMAXIMOPARA_X = 15
VALORMAXIMOPARA_Y = 14
VALORMAXIMOPARA_Z = 5
QUANTIDADE_POPULACAO = 10
QUANTIDADE_MUTACAO = 5
CORTE = 4

# for n in range(0,11):
#     numero = format(n,'b')
#     while numero.__len__() < 4:
#         numero = '0'+numero
#     print('if n == {}:\n\treturn \'{}\'\nel'.format(n,numero),end='')

def printer(l: list):
    for x in l:
        print(x)


def toBin(n):
    numero = format(n, 'b')
    while numero.__len__() < 4:
        numero = '0'+numero
    return numero

def trocaBinToInt(nomeBin):
    decimal = 0
    binario = int(nomeBin)
    i=0
    n=len(str(nomeBin))
    while n>=0:
        resto = binario % 10
        decimal =decimal +(resto * (2**i))
        n=n-1
        i=i+1
        binario=binario//10
    decimal = str(decimal)
    while decimal.__len__() < 4:
        decimal = '0'+decimal
    return int(decimal)



def funcaoFitness(x, y, z, w):
    return 5 * x + y * 2 + w + z ** 3


def rnd(valorMaximo =VALORMAXIMOPARA_XYZW):
    return random.randint(VALORMINIMOPARA_XYZW, valorMaximo)

def cria():
    x = rnd(VALORMAXIMOPARA_X)
    y = rnd(VALORMAXIMOPARA_Y)
    z = rnd(VALORMAXIMOPARA_Z)
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


def corte(num,lista):
    return lista[:num]
def setDict(x=None, y=None,z=None, w=None, bin=None, fit=None):
    return {'x': x, 'y': y,'z':z ,'w':w,'bin': bin, 'fit': fit}
def criaNovaPopulacao(_nova, _corte) :
    c = 0
    t = 4
    for cut in _corte:
        print(cut[4][:-5])
        while c < t:
            _nova.append(setDict(bin='{}{}'.format(
                cut[4][:-5],
                _corte[random.randint(0, _corte.__len__() - 1)][4][cut[4].__len__()-(CORTE+1):]
            )))
            t -= 1
        c += 1
        t = 4
    return _nova
def trocaCaractere(nome: str, posicao, novoCaractere):
    retorno = ''
    c = 0
    while c < nome.__len__():
        if c == posicao:
            retorno = retorno + novoCaractere
        else:
            retorno = retorno + nome[c]
        c += 1
    return retorno

def mutacao(__nova):
    historico = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for contador in range(0, QUANTIDADE_MUTACAO):
        retirar = random.randint(0, historico.__len__() - 1)
        numeroAleatorioDaLista = historico[retirar]
        historico.remove(numeroAleatorioDaLista)
        binarioStr = __nova[numeroAleatorioDaLista].get('bin')
        posicaoDoGene = random.randint(0, binarioStr.__len__() - 1)
        geneQueSeraModificado = binarioStr[posicaoDoGene]

        if geneQueSeraModificado == '1':
            binarioStr = trocaCaractere(binarioStr, posicaoDoGene, '0')
        else:
            binarioStr = trocaCaractere(binarioStr, posicaoDoGene, '1')

        __nova[numeroAleatorioDaLista].update(setDict(bin=binarioStr))
    return __nova
def converteCromossomo(___novaPopulacao):
    for item in ___novaPopulacao:
        cromossomo = item.get('bin')
        x = cromossomo[:4]
        y =  cromossomo[4:8]
        z = cromossomo[8:12]
        w = cromossomo[12:16]
        r = [trocaBinToInt(x),trocaBinToInt(y),trocaBinToInt(z),trocaBinToInt(w)]
        item.update(setDict(r[0], r[1], r[2], r[3],cromossomo,funcaoFitness(r[0], r[1], r[2], r[3])))
    return ___novaPopulacao
def dictToList(dic: dict):
    mat = []
    for d in dic:
        mat.append([d.get('x'), d.get('y'),d.get('z'), d.get('w'), d.get('bin'), d.get('fit')])
    return mat

def verificaFim(matr):
    print(matr[0][5])
    ret=False
    for mt in matr:
        if mt[5]== 185:
            ret=True
    return ret

populacaoInicial = cria_populacao_inicial()
printer(populacaoInicial)
matriz = populacaoInicial
novaPopulacao = []

while verificaFim(matriz) is False:

    melhores = corte(CORTE,populacaoInicial)
    criaNovaPopulacao(novaPopulacao,melhores)
    printer(novaPopulacao)
    mutacao(novaPopulacao)
    print('')
    printer(novaPopulacao)
    converteCromossomo(novaPopulacao)
    printer(novaPopulacao)
    matriz = dictToList(novaPopulacao)
    novaPopulacao = []
    matriz=sorted(matriz, key=lambda w: w[5], reverse=True)

    printer(matriz)



