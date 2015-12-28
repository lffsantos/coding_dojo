import unittest
from caixa_eletronico import CaixaEletronico


class TestCaixaEletronico(unittest.TestCase):

    def setUp(self):
        self.caixa_eletronico = CaixaEletronico()

    def test_saque_valor_invalido(self):
        self.assertEqual(self.caixa_eletronico.saque(15), "não é possível efetuar o saque desse valor")
        self.assertEqual(self.caixa_eletronico.saque(11), "não é possível efetuar o saque desse valor")

    def test_saque_valor_menor_50(self):
        self.assertEqual(self.caixa_eletronico.saque(40), (20, 20))
        self.assertEqual(self.caixa_eletronico.saque(30), (20, 10))

    def test_saque_valor_maior_50_menor_100(self):
        self.assertEqual(self.caixa_eletronico.saque(90), (50, 20, 20))
        self.assertEqual(self.caixa_eletronico.saque(60), (50, 10))

    def test_saque_valor_maior_100(self):
        self.assertEqual(self.caixa_eletronico.saque(440), (100, 100, 100, 100, 20, 20))
        self.assertEqual(self.caixa_eletronico.saque(190), (100, 50, 20, 20))


unittest.main()
