import unittest

from banco.jogador_cauteloso import JogadorCauteloso
from banco.propriedade import Propriedade


class PropriedadeTest(unittest.TestCase):

    def setUp(self):
        self.jogador = JogadorCauteloso("Cauteloso")
        self.propriedade1 = Propriedade("Ponta Verde", 150, 50)
        self.propriedade2 = Propriedade("Ponta Verde", 120, 30)

        self.propriedade1.proprietario = self.jogador

    def test_propridade_nao_esta_disponivel(self):
        self.assertFalse(self.propriedade1.verifica_disponibilidade())

    def test_propridade_esta_disponivel(self):
        self.assertTrue(self.propriedade2.verifica_disponibilidade())
