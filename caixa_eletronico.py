"""
http://dojopuzzles.com/problemas/exibe/caixa-eletronico/
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
"""
cedulas = [100, 50, 20, 10]


def cedula20(valor, saida):
    saida += (20, )
    resto = valor - 20
    saida = saque(resto, saida)
    return saida

def cedula50(valor, saida):
    saida += (50, )
    resto = valor - 50
    saida = saque(resto, saida)
    return saida

def cedula100(valor, saida):
    saida += (100, )
    resto = valor - 100
    saida = saque(resto, saida)
    return saida

def saque(valor, saida=()):
    if valor in cedulas:
        saida += (valor, )
        return saida
    elif valor < 50:
        saida = cedula20(valor, saida)
    elif 50 < valor < 100:
        saida = cedula50(valor, saida)
    else:
        saida = cedula100(valor, saida)

    return saida

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
