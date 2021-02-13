# -*- coding: utf=8 -*-
class Propriedade:

    def __init__(self, nome, valor_venda, valor_aluguel):
        self.nome = nome
        self.proprietario = None
        self.valor_venda = valor_venda
        self.valor_aluguel = valor_aluguel


    def verifica_disponibilidade(self):
        if self.proprietario:
            return True
        return False