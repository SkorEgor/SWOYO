import re


def roman_numerals_to_int(roman_numeral: str):
    """Converting a number from Roman notation to decimal integer notation.

    :param roman_numeral: Roman numeral (example: "IV")
    :type roman_numeral: str

    :rtype: int | None
    :return: numbers in decimal integer notation

    * Valid characters: I, V, X, L, C, D, M.
    * Translation problem -> return None
    """
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  # Таблица перевода

    roman_numeral = roman_numeral.upper()  # Текст в верхний регистр, для таблицы перевода

    # В строке только римские цифры/символы
    if not bool(re.match('^[IVXLCDM]+$', roman_numeral)):
        return

    result = roman_to_int[roman_numeral[0]]
    for i in range(1, len(roman_numeral)):
        if roman_to_int[roman_numeral[i]] > roman_to_int[roman_numeral[i - 1]]:
            # Вычитаем с множителем 2, т.к. до этого прибавили это число
            result += roman_to_int[roman_numeral[i]] - 2 * roman_to_int[roman_numeral[i - 1]]
        else:
            result += roman_to_int[roman_numeral[i]]

    return result
