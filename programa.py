from funcoes import * 

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


frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
     texto = ''
     texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
     texto += '_______________________________      _______________________________\n'

     for linha in range(len(tabuleiro_jogador)):
         jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
         oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
         texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
     return texto

tabuleiro_oponente=posiciona_frota(frota_oponente)
tabuleiro_jogador=posiciona_frota(frota)
jogando=True
Nnavio=0
for tipos in frota_oponente.values():
    for navios in tipos:
        Nnavio+=1
jogadas=[]

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    linha=int(input("Jogador, qual linha deseja atacar? "))
    while linha < 0 or linha > 9:
        print("Linha inválida!")
        linha=int(input("Jogador, qual linha deseja atacar? "))
    coluna=int(input("Jogador, qual coluna deseja atacar? "))
    while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna=int(input("Jogador, qual coluna deseja atacar? "))
    if [linha, coluna] in jogadas:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
    else:
        jogadas.append([linha, coluna])
        tabuleiro_oponente=faz_jogada(tabuleiro_oponente,linha,coluna)
        if Nnavio==afundados(frota_oponente,tabuleiro_oponente):
          print('Parabéns! Você derrubou todos os navios do seu oponente!')
          jogando=False




    

    