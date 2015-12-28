"""
http://dojopuzzles.com/problemas/exibe/caixa-eletronico/
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
"""

cedulas = [100, 50, 20, 10]


def seleciona_cedula(valor, saida, nota):
    saida += (nota, )
    resto = valor - nota
    saida = saque(resto, saida)

    return saida

def saque(valor, saida=()):
    if valor%10 != 0:
        return "não é possível efetuar o saque desse valor"
    if valor in cedulas:
        saida += (valor, )
        return saida
    elif valor < 50:
        saida = seleciona_cedula(valor, saida, 20)
    elif 50 < valor < 100:
        saida = seleciona_cedula(valor, saida, 50)
    else:
        saida = seleciona_cedula(valor, saida, 100)

    return saida

assert saque(15) == "não é possível efetuar o saque desse valor"
assert saque(11) == "não é possível efetuar o saque desse valor"
assert saque(10) == (10 ,)
assert saque(20) == (20, )
assert saque(50) == (50, )
assert saque(100) == (100, )
assert saque(30) == (20, 10)
assert saque(40) == (20, 20)
assert saque(50) == (50, )
assert saque(80) == (50, 20, 10)
assert saque(130) == (100, 20, 10)
assert saque(190) == (100, 50, 20, 20)
assert saque(500) == (100, 100, 100, 100, 100)
assert saque(440) == (100, 100, 100, 100, 20, 20)
