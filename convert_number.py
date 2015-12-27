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
                return self.self.values_indo_to_roman[10] * int(number/10)
            else:
                return self.self.values_indo_to_roman[10] + self.self.values_indo_to_roman[50]
    
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