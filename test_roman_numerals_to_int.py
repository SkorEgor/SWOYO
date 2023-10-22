from roman_numerals_to_int import *
import pytest


# Передали пустую строку
def test_range_does_not_contain_numbers():
    assert roman_numerals_to_int('') is None


# Строка содержит / состоит из лишних символов
string_with_extra_characters = ["dffd", "1XLV", "XL0V", "XLV6bjhj"]


@pytest.mark.parametrize("roman_numeral", string_with_extra_characters)
def test_string_with_extra_characters(roman_numeral):
    assert roman_numerals_to_int(roman_numeral) is None


# Римское число написано в смешанном регистре
mixed_case_15 = ["XV", "xV", "xv"]


@pytest.mark.parametrize("roman_numeral", mixed_case_15)
def test_mixed_case(roman_numeral):
    assert roman_numerals_to_int(roman_numeral) == 15


# Проверка перевода (используя все заявленные символы)
roman_and_int = [('I', 1), ('II', 2), ('III', 3), ('IV', 4), ('V', 5),
                 ('MMMCCCV', 3305), ('MCCCLXXIX', 1379), ('MMMDLXXXVI', 3586)]


@pytest.mark.parametrize("roman_numeral, integer_number", roman_and_int)
def test_translation(roman_numeral, integer_number):
    assert roman_numerals_to_int(roman_numeral) == integer_number
