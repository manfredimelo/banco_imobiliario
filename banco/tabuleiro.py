# -*- coding: utf=8 -*-
import random

from banco.jogador_aleatorio import JogadorAleatorio
from banco.jogador_cauteloso import JogadorCauteloso
from banco.jogador_exigente import JogadorExigente
from banco.jogador_impulsivo import JogadorImpulsivo
from banco.propriedade import Propriedade


class Tabuleiro:

    def __init__(self):
        self.vencedor = None
        self.propriedades = [
            Propriedade('Praia do Francês', 90, 10),
            Propriedade('Barra da Tijuca', 150, 40),
            Propriedade('Praia do Futuro', 130, 30),
            Propriedade('Parque Ibirapuera', 60, 10),
            Propriedade('Iterlagos', 120, 15),
            Propriedade('Morumbi', 200, 55),
            Propriedade('Boa Viagem', 125, 25),
            Propriedade('Ponta Verde', 105, 15),
            Propriedade('Pajuçara', 115, 20),
            Propriedade('Recreios', 190, 51),
            Propriedade('Santos', 150, 51),
            Propriedade('Balneário Camburiú', 150, 55),
            Propriedade('Praia do Gunga', 150, 40),
            Propriedade('Milagres', 180, 51),
            Propriedade('Maragogi', 70, 30),
            Propriedade('Piedade', 120, 35),
            Propriedade('Olinda', 120, 40),
            Propriedade('Praia da Barra', 210, 60),
            Propriedade('Jatiuca', 150, 55),
            Propriedade('Praia da Sereia', 40, 15)
        ]

        self.jogadores = [
            JogadorCauteloso('Cauteloso'),
            JogadorExigente('Exigente'),
            JogadorImpulsivo('Impulsivo'),
            JogadorAleatorio('Aleatório')
        ]
        self.time_out = False
        self.quantidade_rodadas = 0

    def partida(self):
        ordem_jogadores = random.sample(self.jogadores, len(self.jogadores))
        tamanho_tabuleito = len(self.propriedades)
        jogo_em_andamento = True
        rodada = 0
        while jogo_em_andamento:
            rodada += 1
            for jogador in ordem_jogadores:
                dado = random.randint(1, 6)
                jogador.mudar_posicao(dado,tamanho_tabuleito)
                # print(self.propriedades[jogador.posicao]).nome
                if jogador.posicao > 0:
                    propriedade = self.propriedades[jogador.posicao-1]
                    if propriedade.proprietario and propriedade.proprietario != jogador:
                        self.pagar_aluguel(jogador, propriedade)
                    elif jogador.comportamento_compra(propriedade):
                        self.comprar_propriedade(jogador, propriedade)
                    if not jogador.verificacao_saldo_positivo():
                        ordem_jogadores.remove(jogador)
                        self.devolve_propriedades(jogador)
                        if len(ordem_jogadores) == 1:
                            jogo_em_andamento = False


            if rodada == 1000 or len(ordem_jogadores) == 1:
                self.vencedor = ordem_jogadores[0]
                jogo_em_andamento =False
                if rodada == 1000:
                    self.time_out = True
                self.quantidade_rodadas = rodada

        if len(ordem_jogadores) == 1:
            self.vencedor = ordem_jogadores[0]
        else:
            self.vencedor =self.define_vencedor(ordem_jogadores)

    def comprar_propriedade(self, jogador, propriedade):
        propriedade.proprietario = jogador
        jogador.saldo -= propriedade.valor_venda


    def pagar_aluguel(self, jogador, propriedade):
        proprietario = propriedade.proprietario
        jogador.saldo -= propriedade.valor_aluguel
        proprietario.saldo += propriedade.valor_aluguel

    def define_vencedor(self, ordem_jogadores):
        return max(ordem_jogadores, key=lambda jogador: jogador.saldo)

    def devolve_propriedades(self, jogador):
        propriedades = filter(lambda propriedade: propriedade.proprietario==jogador, self.propriedades)
        for propriedade in propriedades:
            propriedade.proprietario = None
