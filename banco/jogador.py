# -*- coding: utf=8 -*-

class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.posicao = 0
        self.saldo = 300

    def verificacao_saldo_positivo(self):
        if self.saldo < 0:
            return False
        return True

    def mudar_posicao(self, dado, tamanho_tabuleiro):
        for p in range(dado):
            self.posicao += 1
            if self.posicao == tamanho_tabuleiro:
                self.posicao = 0
                self.saldo += 100
