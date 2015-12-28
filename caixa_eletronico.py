"""
http://dojopuzzles.com/problemas/exibe/caixa-eletronico/
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
"""


class CaixaEletronico:

    def __init__(self):
        self.cedulas = [100, 50, 20, 10]

    def _seleciona_cedula(self, valor):
        '''
        seleciona cedula a ser impressa
        '''
        if valor < 50:
            nota = 20
        elif 50 < valor < 100:
            nota = 50
        else:
            nota = 100

        return nota

    def _calcula_saque(self, valor , saida):
        '''
        Calcula o saque a ser efetuado e armazena e retorna as notas a serem impressas
        '''
        if valor in self.cedulas:
            saida += (valor, )
            return saida

        nota = self._seleciona_cedula(valor)
        saida += (nota, )
        resto = valor - nota
        return self._calcula_saque(resto, saida)


    def saque(self, valor, saida=()):
        '''
        Recebe o valor do saque a ser efetuado
        '''
        if valor%10 != 0:
            return "não é possível efetuar o saque desse valor"

        saque = self._calcula_saque(valor, saida)

        return saque
