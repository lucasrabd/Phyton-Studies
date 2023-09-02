import random

def inicializarTabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimirTabuleiro(tabuleiro):
    print("   0   1   2")
    for i, linha in enumerate(tabuleiro):
        print(f"{i}  {' | '.join(linha)}")
        if i < 2:
            print("  " + "-" * 11)

def imprimeMenuPrincipal():
    print("Escolha o modo de jogo:\n1. Jogador vs Jogador\n2. Jogador vs Máquina (Nível Fácil)")

def leiaCoordenada(mensagem):
    return int(input(mensagem))

def posicaoValida(tabuleiro, linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' '

def verificaVencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(pos == jogador for pos in linha):
            return True
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    return all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3))

def verificaVelha(tabuleiro):
    return all(pos != ' ' for linha in tabuleiro for pos in linha)

def jogar(tabuleiro, linha, coluna, jogador):
    if posicaoValida(tabuleiro, linha, coluna):
        tabuleiro[linha][coluna] = jogador

def jogadaUsuario(tabuleiro, jogador):
    while True:
        linha = leiaCoordenada("Digite a coordenada da linha: ")
        coluna = leiaCoordenada("Digite a coordenada da coluna: ")
        if posicaoValida(tabuleiro, linha, coluna):
            jogar(tabuleiro, linha, coluna, jogador)
            break
        else:
            print("Posição inválida. Tente novamente.")

def jogadaMaquinaFacil(tabuleiro):
    linha, coluna = random.randint(0, 2), random.randint(0, 2)
    while not posicaoValida(tabuleiro, linha, coluna):
        linha, coluna = random.randint(0, 2), random.randint(0, 2)
    jogar(tabuleiro, linha, coluna, 'O')

def main():
    while True:
        imprimeMenuPrincipal()
        modo = int(input("Digite o número do modo: "))
        jogador1_pontos = jogador2_pontos = 0
        
        while jogador1_pontos < 3 and jogador2_pontos < 3:
            tabuleiro = inicializarTabuleiro()
            jogador_atual = 'X'
            
            while True:
                imprimirTabuleiro(tabuleiro)
                
                if jogador_atual == 'X':
                    print("Jogador 1, é a sua vez.")
                    jogadaUsuario(tabuleiro, jogador_atual)
                else:
                    if modo == 1:
                        print("Jogador 2, é a sua vez.")
                        jogadaUsuario(tabuleiro, jogador_atual)
                    else:
                        print("Máquina, é a sua vez.")
                        jogadaMaquinaFacil(tabuleiro)
                
                if verificaVencedor(tabuleiro, jogador_atual):
                    imprimirTabuleiro(tabuleiro)
                    if jogador_atual == 'X':
                        print("** -- Jogador 1 venceu! -- **")
                        jogador1_pontos += 1
                    else:
                        if modo == 1:
                            print("** -- Jogador 2 venceu! -- **")
                            jogador2_pontos += 1
                        else:
                            print("** -- Máquina venceu! -- **")
                            jogador2_pontos += 1
                    break
                elif verificaVelha(tabuleiro):
                    imprimirTabuleiro(tabuleiro)
                    print("** -- Empate! -- **")
                    break
                
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
            
            print("** -- Pontuação -- **")
            print(f"Jogador 1: {jogador1_pontos}\nJogador 2: {jogador2_pontos}")
            
        resposta = input("** -- Fim do jogo. Deseja jogar novamente? (s/n) -- **").lower()
        if resposta != 's':
            break

if __name__ == "__main__":
    main()
