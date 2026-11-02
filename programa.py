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

print(frota)
    