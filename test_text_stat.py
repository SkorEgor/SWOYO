from text_stat import *
from data_for_tests import *
import pytest

# Проверка на разделение слов
text_and_word_list = [
    ('  ', []),  # Пробелы
    ('Привет', ['Привет']),  # Одно слово
    ('тех кому', ['тех', 'кому']),  # Разделитель пробел
    ('те56х кому78 45fr', ['те56х', 'кому78', '45fr']),  # С цифрами
    ('тех_кому спать', ['тех_кому', 'спать']),  # С нижним подчеркиванием
    ('тех     кому', ['тех', 'кому']),  # Разделитель несколько пробелов
    ('тех, кому', ['тех', 'кому']),  # Разделитель ,
    ('учебу (About', ['учебу', 'About']),  # Разделитель (
    ('фразами? Мотивирующие', ['фразами', 'Мотивирующие']),  # Разделитель ?
    ('учебу (About', ['учебу', 'About']),  # Разделитель .
    ('today, you’ll', ['today', 'you', 'll']),  # you’ll - сокращённая форма you will -> 2 слова
    ('''today 
    
    
    кому''', ['today', 'кому'])  # Разделитель перевод строки
]


@pytest.mark.parametrize('text, word_list', text_and_word_list)
def test_finding_words_from_text(text: str, word_list: list):
    assert word_list_from_text(text) == word_list


def test_empty_text():
    assert word_list_from_text("") == []


def test_counting_letters():
    assert count_of_letter_uses(mixed_text.lower()) == letters_and_number_for_mixed_text


def test_counting_letters_in_empty_text():
    empty_dictionary = {}
    rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in rus_alphabet + eng_alphabet:
        empty_dictionary[i] = 0
    assert count_of_letter_uses("") == empty_dictionary


# Тест на поиск параграфов
paragraphs = [
    ("", 0),
    ("""
    
    
    """, 0),
    ("Привет кот", 1),
    ("    Привет кот", 1),
    ("""
    
Привет кот""", 1),
    ("""

   Привет кот""", 1),
    ("Впервые последний вопрос был задан наполовину", 1),
]


@pytest.mark.parametrize('text_with_paragraphs,count_paragraphs', paragraphs)
def test_number_of_paragraphs(text_with_paragraphs: str, count_paragraphs: int):
    assert number_of_paragraphs(text_with_paragraphs) == count_paragraphs


def test_number_of_paragraphs_in_text():
    assert number_of_paragraphs(mixed_text) == 37


# Поиск слов с русскими и английскими буквами
def test_bilingual_word():
    assert bilingual_word("sdsdfdf ffdfывыв, dffdf ввааав. dsdsddsdsф ававdsd 988989assыфы вывыв95895dsds") == 5

