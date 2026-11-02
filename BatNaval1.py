def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])   
        else:
            posicoes.append([linha, coluna + i])   
    return posicoes 

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho): 
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_navio not in frota: 
        frota[nome_navio] = [] 
    frota[nome_navio].append(posicoes)
    return frota 

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna]==0:
        tabuleiro[linha][coluna]='-'
    elif tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    return tabuleiro
    
def posiciona_frota(dic):
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]
    l=0
    c=0
    for tipo in dic.keys():
        for navio in dic[tipo]:
            for pos in dic[tipo][navio]:
                l=dic[tipo][navio][pos][0]
                c=dic[tipo][navio][pos][1]
                tabuleiro[l][c] = 1
    return tabuleiro


def afundados(dic, tabuleiro):
    i=0
    na=0
    for tipo in dic.keys(): 
        for navio in dic[tipo]:
            i=0
            for l,c in navio:
                if tabuleiro[l][c] !='X':
                    i=1
                    break
            if i==0:
                na +=1
    return na


def posicao_valida(info_navios, linha, coluna, orientacao, tamanho): 
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    for linha, coluna in posicao:
        if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
            return False
    for navios in info_navios.values(): 
        for navio in navios:
            for localizacao in navio:
                if localizacao in posicao:
                    return False    
    return True


navios = {
    "porta-aviões": [1, 4],
    "navio-tanque": [2, 3],
    "contratorpedeiro": [3, 2],
    "submarino": [4, 1],
}

frota = {}
for nome in navios.keys():
    qtd = navios[nome][0]
    tam = navios[nome][1]
    contador = 0
    while contador < qtd: 
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tam}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if tam == 1:
            orientacao = "vertical"
        else:
            opcao = int(input(" [1] Vertical [2] Horizontal: "))
            if opcao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"

        if posicao_valida(frota, linha, coluna, orientacao, tam):
            frota = preenche_frota(frota, nome, linha, coluna, orientacao, tam)
            contador += 1
        else: 
            print("Esta posição não está válida!")

print(frota)
    
