import unittest

from banco.jogador_cauteloso import JogadorCauteloso
from banco.jogador_exigente import JogadorExigente
from banco.jogador_impulsivo import JogadorImpulsivo
from banco.propriedade import Propriedade


class ComportamentoCompraTest(unittest.TestCase):

    def setUp(self):
        self.cauteloso = JogadorCauteloso("Cauteloso")
        self.impulsivo = JogadorImpulsivo("Impulsivo")
        self.exigente = JogadorExigente("Exigente")
        self.aleatorio = JogadorExigente("Aleatório")
        self.propriedade1 = Propriedade("Ponta Verde", 150, 50)
        self.propriedade2 = Propriedade("Ponta Verde", 120, 30)
        self.propriedade3 = Propriedade("Pajuçara", 140, 51)
        self.propriedade4 = Propriedade("Francês", 230, 51)

    def test_cauteloso_compra_se_valor_saldo_apos_compra_maior_igual_80(self):
        comportamento = self.cauteloso.comportamento_compra(self.propriedade3)
        self.assertTrue(comportamento)

    def test_cauteloso_nao_compra_se_valor_saldo_apos_compra_menor_80(self):
        comportamento = self.cauteloso.comportamento_compra(self.propriedade4)
        self.assertFalse(comportamento)

    def test_impulsivo_compra_propriedade_se_tem_saldo(self):
        comportamento = self.impulsivo.comportamento_compra(self.propriedade4)
        self.assertTrue(comportamento)

    def test_impulsivo_nao_compra_propriedade_se_nao_tem_saldo(self):
        self.impulsivo.saldo = 30
        comportamento = self.impulsivo.comportamento_compra(self.propriedade4)
        self.assertFalse(comportamento)

    def test_exigente_compra_se_valor_aluguel_maior_50(self):
        comportamento = self.exigente.comportamento_compra(self.propriedade4)
        self.assertTrue(comportamento)

    def test_exigente_nao_compra_se_valor_aluguel_menor_igual_50(self):
        comportamento = self.exigente.comportamento_compra(self.propriedade1)
        self.assertFalse(comportamento)

    def test_exigente_nao_compra_se_valor_aluguel_maior_50_mas_nao_tem_saldo(self):
        self.exigente.saldo = 10
        comportamento = self.exigente.comportamento_compra(self.propriedade4)
        self.assertFalse(comportamento)

    def test_aleatorio_nao_compra_propriedade_sem_ter_saldo(self):
        self.aleatorio.saldo = 10
        comportamento = self.aleatorio.comportamento_compra(self.propriedade4)
        self.assertFalse(comportamento)

    def test_jogador_saldo_positivo(self):
        self.aleatorio.saldo = 10

        self.assertTrue(self.aleatorio.verificacao_saldo_positivo())

    def test_jogador_muda_posicao_para_zero(self):
        self.exigente.posicao = 15
        self.exigente.mudar_posicao(6, 20)
        self.assertEqual(self.exigente.posicao, 0)

    def test_jogador_ganha_cem_passar_pelo_inicio(self):
        self.aleatorio.posicao = 15
        self.aleatorio.mudar_posicao(6, 20)
        self.assertEqual(self.aleatorio.saldo, 400)

    def test_jogador_nao_ganha_cem__antes_passar_pelo_inicio(self):
        self.aleatorio.posicao = 15
        self.aleatorio.mudar_posicao(5, 20)
        self.assertEqual(self.aleatorio.saldo, 300)