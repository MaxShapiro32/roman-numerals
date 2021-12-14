import unittest
from app.services import data_handler
from app.errors import roman_numeral_error


class TestRomanNumeralsToNumbers(unittest.TestCase):
    '''
    Testing Converting Roman Numerals to Numbers
    /to-number route
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_each_roman_numeral(self):
        '''
        Roman numerals are a number system used by the Roman Empire, based on letters M D C L X V
        '''
        self.assertEqual(data_handler.to_number("I"), 1)
        self.assertEqual(data_handler.to_number("i"), 1)
        self.assertEqual(data_handler.to_number("V"), 5)
        self.assertEqual(data_handler.to_number("X"), 10)
        self.assertEqual(data_handler.to_number("L"), 50)
        self.assertEqual(data_handler.to_number("C"), 100)
        self.assertEqual(data_handler.to_number("D"), 500)
        self.assertEqual(data_handler.to_number("M"), 1000)

    def test_nulla(self):
        '''
        There is no Roman Numeral for the number 0, instead they wrote nulla (the Latin word meaning none)
        '''
        self.assertEqual(data_handler.to_number("nulla"), 0)
        self.assertEqual(data_handler.to_number("NULLA"), 0)
        self.assertEqual(data_handler.to_number("nuLLa"), 0)

    def test_multiple_roman_numeral_characters(self):
        '''
        Roman numerals are read left to right, with higher values being placed before lower values. To get the number represented by the numeral add the individual values together.
        '''
        self.assertEqual(data_handler.to_number("MMDCCLXVIII"), 2768)
        self.assertEqual(data_handler.to_number("MMMCMXCIX"), 3999)

    def test_four_and_nine_roman_numerals(self):
        '''
        One exception to the rule when calculating the roman numeral value is when you want a 4 or 9
        '''
        self.assertEqual(data_handler.to_number("IV"), 4)
        self.assertEqual(data_handler.to_number("IX"), 9)
        self.assertEqual(data_handler.to_number("DXIX"), 519)
        self.assertEqual(data_handler.to_number("CDXLIV"), 444)
        self.assertEqual(data_handler.to_number("CMXCIX"), 999)

    def test_invalid_roman_numerals(self):
        '''
        Roman Numbers don't allow more than 3 consecutive occurrences of the same letter, so you take the next value up and subtract 1. Also if not valid Roman Numeral Character
        '''
        with self.assertRaises(roman_numeral_error.InvalidRomanNumeralException):
             data_handler.to_number("IIIIV")
        with self.assertRaises(roman_numeral_error.InvalidRomanNumeralException):
            data_handler.to_number("XXXX")
        with self.assertRaises(roman_numeral_error.InvalidRomanNumeralException):
            data_handler.to_number("MAX")


if __name__ == "__main__":
    unittest.main()
