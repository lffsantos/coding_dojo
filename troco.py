__author__ = 'lucas'

# http://dojopuzzles.com/problemas/exibe/troco/
# Deve-se considerar que há:
# cédulas de R$100,00, R$50,00, R$10,00, R$5,00 e R$1,00;
# moedas de R$0,50, R$0,10, R$0,05 e R$0,01.

moedas = [0.5, 0.1, 0.05, 0.01]
cedulas = [100, 50, 10, 5, 1]


def get_cedula_or_moeda(valor):
    if valor in moedas+cedulas:
        return valor
    else:
        if valor > 1:
            return get_cedula(valor)
        else:
            return get_moeda(valor)


def get_moeda(valor):
    for m in moedas:
        if valor > m:
            return m
    return None


def get_cedula(valor):
    for c in cedulas:
        if valor > c:
            return c
    return None

def troco(valor_pago, valor_produto):
    troco_cliente = ()
    resto = valor_pago - valor_produto
    resto = round(resto, 2)
    if resto in cedulas:
        return (resto, )
    cedula = get_cedula_or_moeda(resto)
    while cedula:
        troco_cliente += (cedula, )
        resto -= cedula
        resto = abs(round(resto, 2))
        cedula = get_cedula_or_moeda(resto)

    return troco_cliente

assert troco(100, 90) == (10,)
assert troco(100, 80) == (10,10, )
assert troco(100, 75) == (10,10,5)
assert troco(250, 235) == (10,5)
assert troco(50, 45.55) == (1,1,1,1,0.1,0.1,0.1,0.1,0.05)