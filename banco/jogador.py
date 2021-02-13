# -*- coding: utf=8 -*-
class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.posicao = 0
        self.saldo = 300

    def verificacao_saldo_positivo(self):
        return True