import unittest
from convert_number import ConvertNumber


class ConvertNumberTest(unittest.TestCase):

    def setUp(self):
        self.convert_number = ConvertNumber()

    def test_convert_to_roman(self):
        self.assertEqual(self.convert_number.convert_to_roman(1), 'I')

    def test__convert_greater_50_less_100(self):
        self.assertEqual(self.convert_number._convert_greater_50_less_100(88, []), 'LXXXVIII')

    def test__convert_greater_100_less_500(self):
        self.assertEqual(self.convert_number._convert_greater_100_less_500(367, []), 'CCCLXVII')

    def test__convert_greater_500_less_1000(self):
        self.assertEqual(self.convert_number._convert_greater_500_less_1000(894, []), 'DCCCXCIV')

    def test__convert_greater_1000_less_4000(self):
        self.assertEqual(self.convert_number._convert_greater_1000_less_4000(3899), 'MMMDCCCXCIX')

    def test__convert_greater_4000(self):
        self.assertEqual(self.convert_number._convert_greater_4000(1550500), '(MDL)D')



# assert convert_to_roman(1) == 'I'
# assert convert_to_roman(5) == 'V'
# assert convert_to_roman(10) == 'X'
# assert convert_to_roman(2) == 'II'
# assert convert_to_roman(3) == 'III'
# assert convert_to_roman(4) == 'IV'
# assert convert_to_roman(6) == 'VI'
# assert convert_to_roman(7) == 'VII'
# assert convert_to_roman(8) == 'VIII'
# assert convert_to_roman(9) == 'IX'
# assert convert_to_roman(11) == 'XI'
# assert convert_to_roman(12) == 'XII'
# assert convert_to_roman(13) == 'XIII'
# assert convert_to_roman(14) == 'XIV'
# assert convert_to_roman(15) == 'XV'
# assert convert_to_roman(16) == 'XVI'
# assert convert_to_roman(17) == 'XVII'
# assert convert_to_roman(18) == 'XVIII'
# assert convert_to_roman(19) == 'XIX'
# assert convert_to_roman(20) == 'XX'
# assert convert_to_roman(21) == 'XXI'
# assert convert_to_roman(27) == 'XXVII'
# assert convert_to_roman(28) == 'XXVIII'
# assert convert_to_roman(29) == 'XXIX'
# assert convert_to_roman(30) == 'XXX'
# assert convert_to_roman(31) == 'XXXI'
# assert convert_to_roman(34) == 'XXXIV'
# assert convert_to_roman(37) == 'XXXVII'
# assert convert_to_roman(39) == 'XXXIX'
# assert convert_to_roman(40) == 'XL'
# assert convert_to_roman(41) == 'XLI'
# assert convert_to_roman(44) == 'XLIV'
# assert convert_to_roman(47) == 'XLVII'
# assert convert_to_roman(49) == 'XLIX'
# assert convert_to_roman(50) == 'L'
# assert convert_to_roman(51) == 'LI'
# assert convert_to_roman(54) == 'LIV'
# assert convert_to_roman(60) == 'LX'
# assert convert_to_roman(60) == 'LX'
# assert convert_to_roman(70) == 'LXX'
# assert convert_to_roman(80) == 'LXXX'
# assert convert_to_roman(73) == 'LXXIII'
# assert convert_to_roman(69) == 'LXIX'
# assert convert_to_roman(88) == 'LXXXVIII'
# assert convert_to_roman(90) == 'XC'
# assert convert_to_roman(93) == 'XCIII'
# assert convert_to_roman(97) == 'XCVII'
# assert convert_to_roman(99) == 'XCIX'
# assert convert_to_roman(100) == 'C'
# assert convert_to_roman(200) == 'CC'
# assert convert_to_roman(300) == 'CCC'
# assert convert_to_roman(400) == 'CD'
# assert convert_to_roman(149) == 'CXLIX'
# assert convert_to_roman(101) == 'CI'
# assert convert_to_roman(110) == 'CX'
# assert convert_to_roman(115) == 'CXV'
# assert convert_to_roman(119) == 'CXIX'
# assert convert_to_roman(222) == 'CCXXII'
# assert convert_to_roman(367) == 'CCCLXVII'
# assert convert_to_roman(498) == 'CDXCVIII'
# assert convert_to_roman(894) == 'DCCCXCIV'
# assert convert_to_roman(501) == 'DI'
# assert convert_to_roman(521) == 'DXXI'
# assert convert_to_roman(578) == 'DLXXVIII'
# assert convert_to_roman(600) == 'DC'
# assert convert_to_roman(700) == 'DCC'
# assert convert_to_roman(800) == 'DCCC'
# assert convert_to_roman(900) == 'CM'
# assert convert_to_roman(972) == 'CMLXXII'
# assert convert_to_roman(2000) == 'MM'
# assert convert_to_roman(2500) == 'MMD'
# assert convert_to_roman(2577) == 'MMDLXXVII'
# assert convert_to_roman(2899) == 'MMDCCCXCIX'
# assert convert_to_roman(3899) == 'MMMDCCCXCIX'
# assert convert_to_roman(4000) == '(IV)'
# assert convert_to_roman(4500) == '(IV)D'
# assert convert_to_roman(5000) == '(V)'
# assert convert_to_roman(6000) == '(VI)'
# assert convert_to_roman(1550500) == '(MDL)D'
# assert convert_to_roman(15505000) == '((XV)DV)'
# assert convert_to_roman(749705) == '(DCCXLIX)DCCV'
# assert convert_to_roman(58037) == '(LVIII)XXXVII'
# assert convert_to_roman(981113000) == '((CMLXXXI)CXIII)'

