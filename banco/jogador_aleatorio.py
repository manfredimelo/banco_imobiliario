# -*- coding: utf=8 -*-
from banco.jogador import Jogador
import random

class JogadorCauteloso(Jogador):

    def __init__(self, nome):
        return super().__init__(nome)

    def comportamento_compra(self, propriedade):
        if  propriedade.verifica_disponibilidade() and self.verificacao_saldo_positivo() \
                and self.aleatorio:
            return True
        return False
    def aleatorio(self):
        return random.choice([True, False])