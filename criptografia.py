"""
Matriz base para o algoritmo:

    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E   E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F   F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G   G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H   H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I   I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J   J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K   K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L   L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M   M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N   N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O   O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P   P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q   Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R   R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S   S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T   T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U   U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V   V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W   W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X   X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y   Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z   Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

Para o exemplo  o texto plano PERDAO e a chave criptográfica LIMAO.

Para cada letra combine a chave e o texto a ser criptografado, se necessário repita a chave até que ela cubra todo o texto:

LIMAO
PERDAO

   Procure a coluna com a letra do texto a ser criptografada, no nosso caso P.
   Ande na coluna até encontrar a letra correspondente da chave, novamente no exemplo, a letra L
   O índice da linha será o valor criptografado, no caso, a letra W.
   Repita com todas as letras do texto a ser criptografado.

Desta forma o resultado da criptografia deverá ser:

WEVXOX
"""
__author__ = 'lucas'

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def criptografa_palavra(palavra, key):
    key_dict = { k[0]:k[1] for k in enumerate([ a for a in key])}
    i = 0
    new_palavra = ''
    for p in palavra:
        index = alphabet.index(p)
        new_alphabet = alphabet[index:] + alphabet[0:index]

        index2 = key_dict.get(i)
        if not index2:
            i = 0
            index2 = key_dict.get(i)
        else:
            i +=1
        index2 = new_alphabet.index(index2)

        new_palavra += alphabet[index2]

    return new_palavra

if __name__ == '__main__':

    assert criptografa_palavra('PERDAO', 'LIMAO') == 'WEVXOX'
    assert criptografa_palavra('LIMAO', 'CASA') == 'RSGAO'
    assert criptografa_palavra('DADO', 'CASA') == 'ZAPM'

