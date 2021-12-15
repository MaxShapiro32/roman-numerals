from app.errors import roman_numeral_error
import re

roman_numeral_value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
roman_numeral_special_value_map = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}

def get_data(context):
    context.start("getData")
    context.stop()
    #raise example_error.ExampleException("TODO: Implement me!")


def to_number(roman_numeral):
    roman_numeral = roman_numeral.upper()
    result = 0

    if str(roman_numeral).lower() == "nulla":
        return result

    if not _is_valid_roman_numeral(roman_numeral):
        raise roman_numeral_error.InvalidRomanNumeralException("Error: Invalid Roman Numeral")

    for key in list(roman_numeral_special_value_map.keys()):
        if key in roman_numeral:
            roman_numeral = roman_numeral.replace(key,"")
            result += roman_numeral_special_value_map[key]

    for letter in roman_numeral:
        if letter not in roman_numeral_value_map.keys():
            raise  roman_numeral_error.InvalidRomanNumeralException("Error: Invalid Roman Numeral")
        result += roman_numeral_value_map[letter]

    return result


def to_roman_numeral(number):
    result = ""

    if not _is_valid_number(number):
        raise roman_numeral_error.InvalidNumberException("Error: Invalid Number")

    if number == 0:
        return "nulla"

    roman_sorted = sorted(roman_numeral_value_map.items() | roman_numeral_special_value_map.items(), key=lambda x: x[1], reverse=True)

    for numeral in roman_sorted:
        while number >= numeral[1]:
            result += numeral[0]
            number -= numeral[1]


    return result


def _is_valid_roman_numeral(roman_numeral):
    is_valid = re.match(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', roman_numeral)
    if is_valid:
        return True
    return False


def _is_valid_number(number):
    if number < 0 or number > 3999 or isinstance(number, float):
        return False
    return True


def readiness_check():
    return True
