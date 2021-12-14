from app.errors import roman_numeral_error

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

    consecutive_check = ("",0)
    for letter in roman_numeral:
        if letter == consecutive_check[0]:
            consecutive_check = (letter, consecutive_check[1]+1)
        else:
            consecutive_check = (letter,1)
        if consecutive_check[1] == 4:
            raise roman_numeral_error.InvalidRomanNumeralException("Error: Invalid Roman Numeral")

    for key in list(roman_numeral_special_value_map.keys()):
        if key in roman_numeral:
            roman_numeral = roman_numeral.replace(key,"")
            result += roman_numeral_special_value_map[key]

    for letter in roman_numeral:
        if letter not in roman_numeral_value_map.keys():
            raise roman_numeral_error.InvalidRomanNumeralException("Error: Invalid Roman Numeral")
        result += roman_numeral_value_map[letter]

    return result


def readiness_check():
    return True
