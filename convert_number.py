""" Explicação do Problema
http://dojopuzzles.com/problemas/exibe/numeros-romanos/
"""


class ConvertNumber:
    
    def __init__(self):
        self.values_indo_to_roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    
    def _converter(self, number, roman_number):
        str_number = str(number)
        last_digit = str_number[-1]
        new_number = number - int(last_digit)
        if new_number == number:
            last_digit = str_number[-2:]
            new_number = number - int(last_digit)
    
        roman_number.append(self.convert_to_roman(int(last_digit)))
        roman_number.append(self.convert_to_roman(new_number))
        return ''.join(roman_number[::-1])

    def _convert_smaller_50(self, number, roman_number):
        '''
        Converte numeros menores do que 50
        '''
        if str(number)[-1] == '0':
            if int(number/10) <= 3:
                return self.values_indo_to_roman[10] * int(number/10)
            else:
                return self.values_indo_to_roman[10] + self.values_indo_to_roman[50]
    
        return self._converter(number, roman_number)
    
    def _convert_greater_50_less_100(self, number, roman_number):
        """
        Converte numeros entre 50 e 100
        """
        if str(number)[-1] == '0':
            if int((number-50)/10) <= 3:
                return self.values_indo_to_roman[50] + self.values_indo_to_roman[10] * int((number-50)/10)
            else:
                return self.values_indo_to_roman[10] + self.values_indo_to_roman[100]
    
        return self._converter(number, roman_number)
    
    def _convert_greater_100_less_500(self, number, roman_number):
        """
        Converte numeros entre 100 e 500
        """
        if number % 100 == 0:
            if (number - 100)/100 < 3:
                return self.values_indo_to_roman[100] * (int((number - 100)/100)+1)
            else:
                return self.values_indo_to_roman[100] + self.values_indo_to_roman[500]
    
        return self._converter(number, roman_number)
    
    def _convert_greater_500_less_1000(self, number, roman_number):
        """
        Converte numeros entre 500 e 1000
        """
        if number % 100 == 0:
            if (number - 500)/100 <= 3:
                return self.values_indo_to_roman[500] + self.values_indo_to_roman[100]* int((number - 500)/100)
            else:
                return self.values_indo_to_roman[100] + self.values_indo_to_roman[1000]
    
        return self._converter(number, roman_number)
    
    def _convert_greater_1000_less_4000(self, number):
        """
        Converte numeros entre 1000 e 4000
        """
        return int(str(number)[0]) * self.values_indo_to_roman[1000] + self.convert_to_roman(number%1000)
    
    def _convert_greater_4000(self, number):
        """
        Converte numeros maiores do que 4000
        """
        div = self.convert_to_roman(int(number/1000))
        rest = self.convert_to_roman(number % 1000)
        return "("+div+")" + rest

    def convert_to_roman(self, number):
        """
        Converte um numero decimal em romano
        """
        roman_number = []
        if self.values_indo_to_roman.get(number):
            return self.values_indo_to_roman.get(number)
        elif number in (2, 3):
            return 'I'*number
        elif number == 4:
            return 'IV'
        elif number in (6, 7, 8):
            return 'V' + (self.values_indo_to_roman[1] * ( number - 5))
        elif number == 9:
            return 'IX'
        else:
            if number < 50:
                return self._convert_smaller_50(number, roman_number)
            elif 50 < number < 100:
                return self._convert_greater_50_less_100(number, roman_number)
            elif 100 < number < 500:
                return self._convert_greater_100_less_500(number, roman_number)
            elif 500 < number < 1000:
                return self._convert_greater_500_less_1000(number, roman_number)
            elif 1000 < number < 4000:
                return self._convert_greater_1000_less_4000(number)
    
        return self._convert_greater_4000(number)


# Testes:

#############################

# Cria uma instância da classe ConvertNumber
conversor = ConvertNumber()

assert conversor.convert_to_roman(1) == 'I'
assert conversor.convert_to_roman(5) == 'V'
assert conversor.convert_to_roman(10) == 'X'
assert conversor.convert_to_roman(2) == 'II'
assert conversor.convert_to_roman(3) == 'III'
assert conversor.convert_to_roman(4) == 'IV'
assert conversor.convert_to_roman(6) == 'VI'
assert conversor.convert_to_roman(7) == 'VII'
assert conversor.convert_to_roman(8) == 'VIII'
assert conversor.convert_to_roman(9) == 'IX'
assert conversor.convert_to_roman(11) == 'XI'
assert conversor.convert_to_roman(12) == 'XII'
assert conversor.convert_to_roman(13) == 'XIII'
assert conversor.convert_to_roman(14) == 'XIV'
assert conversor.convert_to_roman(15) == 'XV'
assert conversor.convert_to_roman(16) == 'XVI'
assert conversor.convert_to_roman(17) == 'XVII'
assert conversor.convert_to_roman(18) == 'XVIII'
assert conversor.convert_to_roman(19) == 'XIX'
assert conversor.convert_to_roman(20) == 'XX'
assert conversor.convert_to_roman(21) == 'XXI'
assert conversor.convert_to_roman(27) == 'XXVII'
assert conversor.convert_to_roman(28) == 'XXVIII'
assert conversor.convert_to_roman(29) == 'XXIX'
assert conversor.convert_to_roman(30) == 'XXX'
assert conversor.convert_to_roman(31) == 'XXXI'
assert conversor.convert_to_roman(34) == 'XXXIV'
assert conversor.convert_to_roman(37) == 'XXXVII'
assert conversor.convert_to_roman(39) == 'XXXIX'
assert conversor.convert_to_roman(40) == 'XL'
assert conversor.convert_to_roman(41) == 'XLI'
assert conversor.convert_to_roman(44) == 'XLIV'
assert conversor.convert_to_roman(47) == 'XLVII'
assert conversor.convert_to_roman(49) == 'XLIX'
assert conversor.convert_to_roman(50) == 'L'
assert conversor.convert_to_roman(51) == 'LI'
assert conversor.convert_to_roman(54) == 'LIV'
assert conversor.convert_to_roman(60) == 'LX'
assert conversor.convert_to_roman(60) == 'LX'
assert conversor.convert_to_roman(70) == 'LXX'
assert conversor.convert_to_roman(80) == 'LXXX'
assert conversor.convert_to_roman(73) == 'LXXIII'
assert conversor.convert_to_roman(69) == 'LXIX'
assert conversor.convert_to_roman(88) == 'LXXXVIII'
assert conversor.convert_to_roman(90) == 'XC'
assert conversor.convert_to_roman(93) == 'XCIII'
assert conversor.convert_to_roman(97) == 'XCVII'
assert conversor.convert_to_roman(99) == 'XCIX'
assert conversor.convert_to_roman(100) == 'C'
assert conversor.convert_to_roman(200) == 'CC'
assert conversor.convert_to_roman(300) == 'CCC'
assert conversor.convert_to_roman(400) == 'CD'
assert conversor.convert_to_roman(149) == 'CXLIX'
assert conversor.convert_to_roman(101) == 'CI'
assert conversor.convert_to_roman(110) == 'CX'
assert conversor.convert_to_roman(115) == 'CXV'
assert conversor.convert_to_roman(119) == 'CXIX'
assert conversor.convert_to_roman(222) == 'CCXXII'
assert conversor.convert_to_roman(367) == 'CCCLXVII'
assert conversor.convert_to_roman(498) == 'CDXCVIII'
assert conversor.convert_to_roman(894) == 'DCCCXCIV'
assert conversor.convert_to_roman(501) == 'DI'
assert conversor.convert_to_roman(521) == 'DXXI'
assert conversor.convert_to_roman(578) == 'DLXXVIII'
assert conversor.convert_to_roman(600) == 'DC'
assert conversor.convert_to_roman(700) == 'DCC'
assert conversor.convert_to_roman(800) == 'DCCC'
assert conversor.convert_to_roman(900) == 'CM'
assert conversor.convert_to_roman(972) == 'CMLXXII'
assert conversor.convert_to_roman(2000) == 'MM'
assert conversor.convert_to_roman(2500) == 'MMD'
assert conversor.convert_to_roman(2577) == 'MMDLXXVII'
assert conversor.convert_to_roman(2899) == 'MMDCCCXCIX'
assert conversor.convert_to_roman(3899) == 'MMMDCCCXCIX'
assert conversor.convert_to_roman(4000) == '(IV)'
assert conversor.convert_to_roman(4500) == '(IV)D'
assert conversor.convert_to_roman(5000) == '(V)'
assert conversor.convert_to_roman(6000) == '(VI)'
assert conversor.convert_to_roman(1550500) == '(MDL)D'
assert conversor.convert_to_roman(15505000) == '((XV)DV)'
assert conversor.convert_to_roman(749705) == '(DCCXLIX)DCCV'
assert conversor.convert_to_roman(58037) == '(LVIII)XXXVII'
assert conversor.convert_to_roman(981113000) == '((CMLXXXI)CXIII)'