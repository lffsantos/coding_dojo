__author__ = 'lucas'
from collections import defaultdict

dict_key = defaultdict(list)
global old_size
old_size = 0

def split_lista(lista2, value):
    global old_size
    for i in range(len(lista2)):
        size = abs(value - lista2[i])
        if old_size == 0 or size <= old_size:
            dict_key[size].extend([value, lista2[i]])
            if size != old_size and old_size != 0:
                del dict_key[old_size]
            old_size = size


def calcula_valor(lista):
    lista.sort()
    for i in range(len(lista)):
        split_lista(lista[i+1:], lista[i])

    output = list(dict_key.values())
    output[0].sort()
    new_list = [ str(o) for o in output[0]]
    return ' '.join(new_list)


if __name__ == '__main__':
    assert calcula_valor([100, 70, 20, 23, 2, 5]) == '2 5 20 23'
    assert calcula_valor([1, 4, 6, 7, 10, 100, 70, 20, 23, 2, 5]) == '1 2 4 5 5 6 6 7'