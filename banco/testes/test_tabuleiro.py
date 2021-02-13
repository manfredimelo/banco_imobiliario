import unittest

from banco.tabuleiro import Tabuleiro


class TabuleiroTest(unittest.TestCase):

    def test_partida_nao_iniciada_sem_vendedor(self):
        jogo = Tabuleiro()
        self.assertIsNone(jogo.vencedor)

    def test_partida_completa_com_vendedor(self):
        jogo = Tabuleiro()
        jogo.partida()
        self.assertIsNotNone(jogo.vencedor)