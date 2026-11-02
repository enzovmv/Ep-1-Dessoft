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
            

