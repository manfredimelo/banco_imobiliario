# -*- coding: utf=8 -*-

from banco.tabuleiro import Tabuleiro

def porcentagem(valor):
    if valor:
        return str(round(valor*100/300, 2)) + ' %'
    return 0


def Jogar():
    quantidade_timeout = 0
    quantidade_turnos = 0
    vitorias = {
        'Cauteloso': 0,
        'Exigente': 0,
        'Impulsivo': 0,
        'Aleatório': 0,
    }
    for i in range(0, 300):
        tabuleiro = Tabuleiro()
        tabuleiro.partida()
        if tabuleiro.time_out:
            quantidade_timeout += 1
        quantidade_turnos += tabuleiro.quantidade_rodadas
        vencendor = tabuleiro.vencedor.nome
        if vencendor == 'Cauteloso':
            vitorias['Cauteloso']+=1
        elif vencendor == 'Exigente':
            vitorias['Exigente'] += 1
        elif vencendor == 'Impulsivo':
            vitorias['Impulsivo'] += 1
        elif vencendor == 'Aleatório':
            vitorias['Aleatório'] += 1


    print('Quantidade de time outs: ', quantidade_timeout)
    print('Média de Turnos: ', quantidade_turnos/300)
    for perfil in vitorias:
        print('Perfil {}   Porcentagem: {}'.format(perfil, porcentagem(vitorias[perfil])))
    print('Perfil que mais vence: ', max(vitorias, key=vitorias.get))

if __name__ == "__main__":
    Jogar()

