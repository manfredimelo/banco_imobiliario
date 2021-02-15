import unittest

from banco.tabuleiro import Tabuleiro


class TabuleiroTest(unittest.TestCase):

    def test_partida_nao_iniciada_sem_vencedor(self):
        jogo = Tabuleiro()
        self.assertIsNone(jogo.vencedor)

    def test_partida_completa_com_vencedor(self):
        jogo = Tabuleiro()
        jogo.partida()
        self.assertIsNotNone(jogo.vencedor)

    def test_quantidade_de_propriedades_deve_ser_igual_20(self):
        jogo = Tabuleiro()
        self.assertEqual(len(jogo.propriedades), 20)

    def test_quantidade_de_jogadores_deve_ser_igual_4(self):
        jogo = Tabuleiro()
        self.assertEqual(len(jogo.jogadores), 4)

    def test_posicao_jogadores_deve_ser_igual_0(self):
        jogo = Tabuleiro()
        for jogador in jogo.jogadores:
            self.assertEqual(jogador.posicao, 0)

    def test_posicao_jogadores_deve_ser_igual_300(self):
        jogo = Tabuleiro()
        for jogador in jogo.jogadores:
            self.assertEqual(jogador.saldo, 300)

    def test_posse_jogador_compra_propriedade(self):
        jogo = Tabuleiro()
        jogador = jogo.jogadores[0]
        propriedade = jogo.propriedades[0]
        jogo.comprar_propriedade(jogador, propriedade)
        self.assertEqual(propriedade.proprietario, jogador)

    def test_valor_debitado_jogador_apos_compra_propriedade(self):
        jogo = Tabuleiro()
        jogador = jogo.jogadores[0]
        propriedade = jogo.propriedades[0]
        jogo.comprar_propriedade(jogador, propriedade)
        self.assertEqual(jogador.saldo, 300 - propriedade.valor_venda)

    def test_valor_debitado_jogador_apos_pagar_aluguel(self):
        jogo = Tabuleiro()
        jogador = jogo.jogadores[0]
        propriedade = jogo.propriedades[0]
        propriedade.proprietario = jogo.jogadores[1]
        jogo.pagar_aluguel(jogador, propriedade)
        self.assertEqual(jogador.saldo, 300 - propriedade.valor_aluguel)

    def test_devolve_propriedades(self):
        jogo = Tabuleiro()
        jogador = jogo.jogadores[0]
        propriedade = jogo.propriedades[0]
        propriedade.proprietario = jogo.jogadores[0]
        jogo.devolve_propriedades(jogador)
        self.assertIsNone(propriedade.proprietario)

    def test_define_vencedor(self):
        jogo = Tabuleiro()
        jogador1 = jogo.jogadores[0]
        jogador2 = jogo.jogadores[1]
        jogador3 = jogo.jogadores[2]
        jogador4 = jogo.jogadores[3]
        ordem_jogadores = [jogador1, jogador2, jogador3, jogador4]
        jogador1.saldo =50
        jogador2.saldo = 0
        jogador3.saldo =500
        jogador4.saldo = 0
        self.assertEqual(jogo.define_vencedor(ordem_jogadores), jogador3)

    def test_define_vencedor_desempate(self):
        jogo = Tabuleiro()
        jogador1 = jogo.jogadores[0]
        jogador2 = jogo.jogadores[1]
        jogador3 = jogo.jogadores[2]
        jogador4 = jogo.jogadores[3]
        ordem_jogadores = [jogador1, jogador2, jogador3, jogador4]
        jogador1.saldo =50
        jogador2.saldo = 0
        jogador3.saldo =500
        jogador4.saldo = 500
        self.assertEqual(jogo.define_vencedor(ordem_jogadores), jogador3)