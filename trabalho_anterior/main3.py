import random

intt = 0
matriz = []


def dictToList(dic: dict):
    mat = []
    for d in dic:
        mat.append([d.get('x'), d.get('y'), d.get('bin'), d.get('fit')])
    return mat

def printaBem(nome,x:list):
    print('==== ' + nome)

    printItens(x)
    print('------------------------------')

def verificaFim(matr):
    if matr[0][0] == 2 and matr[0][1] == 3:
        return True
    return False

def funcaoFitness(x, y):
    return 2 - (x - 2) ** 2 - (y - 3) ** 2

def verificaFim(matr):
    if matr[0][0] == 2 and matr[0][1] == 3:
        return True
    return False

def toBin(num: int):
    return num.__str__() \
        .replace('0', '000') \
        .replace('1', '001') \
        .replace('2', '010') \
        .replace('3', '011') \
        .replace('4', '100') \
        .replace('5', '101') \
        .replace('6', '110') \
        .replace('7', '111')


def linha():
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    cromossomo = '{}{}'.format(toBin(x), toBin(y))
    return [x, y, cromossomo, funcaoFitness(x, y)]


def formar_matriz(matriz_):
    for y in range(0, 10):
        matriz_.append(linha())
    return matriz_


def printItens(l: list):
    for x in l:
        print('| x  |  y  | Binario | Fitness |\n  {}    {}     {}      {}\n'
              '------------------------------'.format(x[0],x[1],x[2],x[3]).replace('None','#'))

def setDict(x=None, y=None, bin=None, fit=None):
    return {'x': x, 'y': y, 'bin': bin, 'fit': fit}



matriz = formar_matriz(matriz)
print('Legenda: # - Sem valor')
printaBem('Matriz inicial gerada aleatoriamente',matriz)

while verificaFim(matriz) is False:

    matriz = sorted(matriz, key=lambda w: w[3], reverse=True)
    printaBem('Matriz após ser ordenada',matriz)
    corte = matriz[:4]
    printaBem('Matriz corte 4 primeiros',corte)
    def trocaCaractere(nome:str,posicao,novoCaractere):
        retorno = ''
        c = 0
        while c < nome.__len__():
            if c == posicao:
                retorno = retorno + novoCaractere
            else:
                retorno = retorno + nome[c]
            c+=1
        return retorno


    def criaNovaPopulacao(corte):
        c = 0
        t = 4
        for cut in corte:
            while c < t:
                novaPopulacao.append(setDict(bin='{}{}'.format(
                    cut[2][:-2],
                    corte[random.randint(0, corte.__len__() - 1)][2][4:]
                )))
                t -= 1
            c += 1
            t = 4;

    novaPopulacao = []

    criaNovaPopulacao(corte)

    printaBem('Nova populacao Gerada pelo corte',dictToList(novaPopulacao))

    def mutacao():
        historico = [0,1,2,3,4,5,6,7,8,9]
        for contador in range(0,5):
            retirar = random.randint(0, historico.__len__() - 1)
            numeroAleatorioDaLista = historico[retirar]
            historico.remove(numeroAleatorioDaLista)
            binarioStr = novaPopulacao[numeroAleatorioDaLista].get('bin')
            posicaoDoGene = random.randint(0, binarioStr.__len__() - 1)
            geneQueSeraModificado = binarioStr[posicaoDoGene]


            if geneQueSeraModificado == '1':
                binarioStr = trocaCaractere(binarioStr,posicaoDoGene,'0')
            else:
                binarioStr = trocaCaractere(binarioStr, posicaoDoGene, '1')

            novaPopulacao[numeroAleatorioDaLista].update(setDict(bin=binarioStr))
        return novaPopulacao

    novaPopulacao = mutacao()

    printaBem('Nova populacao com 5 mutações',dictToList(novaPopulacao))

    def trocaBinToInt(nomeBin: str):
        if nomeBin == '000':
            return 0
        elif nomeBin == '001':
            return 1
        elif nomeBin == '010':
            return 2
        elif nomeBin == '011':
            return 3
        elif nomeBin == '100':
            return 4
        elif nomeBin == '101':
            return 5
        elif nomeBin == '110':
            return 6
        elif nomeBin == '111':
            return 7



    def converteCromossomo(__novaPop):
        for item in __novaPop:
            strParaGerarXeY = item.get('bin')
            _3Primeiros = strParaGerarXeY[:3]
            _3Ultimos =  strParaGerarXeY[-3:]
            r = [trocaBinToInt(_3Primeiros),trocaBinToInt(_3Ultimos)]
            item.update(setDict(r[0],r[1],strParaGerarXeY,funcaoFitness(r[0],r[1])))
        return __novaPop

    novaPopulacao = converteCromossomo(novaPopulacao)

    matriz = dictToList(novaPopulacao)
    intt +=1
    print('({}) | x:{}, y:{}'.format(intt,matriz[0][0],matriz[0][1]))