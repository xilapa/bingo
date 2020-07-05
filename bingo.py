import numpy as np

def imprimiCartela(_cartelas):
    i = 1
    for _cartela in _cartelas:
        print(f'Cartela #{i}\n{_cartela}\n')
        i += 1

zeroTres = range(0,3)

# criando lista vazia
cartelas = []

# preenchendo a lista com cartelas(matrizes 3x3)
for i in zeroTres:
    cartelas.append(np.zeros((3,3)))

print('Cartelas Vazias')
imprimiCartela(cartelas)

for cartela in zeroTres:
    # garantindo valores unicos
    while True:
            numeros = np.unique(np.random.randint(0,100,9))
            if np.size(numeros) == 9:
                break   
    inicio = 0
    fim = 3
    for linha in zeroTres:        
        cartelas[cartela][linha,:] = numeros[inicio:fim]
        inicio +=3
        fim += 3

print('\nCartelas Cheias')
imprimiCartela(cartelas)

pontosCartela = [[],[],[]]
ganhador = ''
while ganhador == '':
    pedra = np.random.randint(0,100,1)
    print('\nNúmero sorteado:',pedra)
    for indiceCartela in zeroTres:
        if pedra in cartelas[indiceCartela]:
            pontosCartela[indiceCartela].append(1)
            # TODO: pintarCartela()
    # Modularizar
    for indiceListaPontos in zeroTres:
        pontos = np.sum(pontosCartela[indiceListaPontos])
        print('\tPontos na cartela',indiceListaPontos+1,':',pontos)
        if  pontos == 9:
            ganhador = indiceListaPontos+1
        # ganha quem marcar a cartela toda primeiro
    if ganhador:
        print('\nCartela Ganhadora:',ganhador)