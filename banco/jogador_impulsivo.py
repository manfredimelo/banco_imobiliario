# -*- coding: utf=8 -*-
from banco.jogador import Jogador


class JogadorImpulsivo(Jogador):

    def __init__(self, nome):
        return super().__init__(nome)

    def comportamento_compra(self, propriedade):
        if  propriedade.verifica_disponibilidade() and self.verificacao_saldo_positivo() \
                and (self.saldo - propriedade.valor_venda) >= 0:
            return True
        return False
