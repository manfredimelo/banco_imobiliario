# -*- coding: utf=8 -*-
from banco.jogador import Jogador


class JogadorExigente(Jogador):

    def __init__(self, nome):
        return super().__init__(nome)

    def comportamento_compra(self, propriedade):
        if  propriedade.verifica_disponibilidade() and propriedade.valor_aluguel >50 \
                and self.verificacao_saldo_positivo():
            return True
        return False