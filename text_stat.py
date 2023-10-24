import re

russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
english_alphabet = "abcdefghijklmnopqrstuvwxyz"
rus_and_en_alphabet = russian_alphabet + english_alphabet


def word_list_from_text(text: str):
    """Number of words in the text

    :rtype: list[str]
    :return: numbers in decimal integer notation

    * No words -> []
    """
    return re.findall(r"(\w[\w']*\w|\w)", text)


def count_of_letter_uses(text: str):
    """For letters of the Russian and English alphabet, finds their count  in the text.

    :param text: lowercase text to count letters
    :type text: str

    :rtype: dict
    :return: letter: number of letters in text { str: int }

    * No letters -> {"letter": 0}
    """
    return {letter: text.count(letter) for letter in rus_and_en_alphabet}


def number_words_with_letter(word_list: list, letter: str):
    """Count of words with this letter.

    :param word_list: list of all words from the text
    :type word_list: list[str]

    :param letter: letter we look for in words
    :type letter: str

    :rtype: int
    :return: count of words with this letter
    """
    # Нет проверки на входные параметры
    return sum(map(lambda word: letter in word, word_list))


def frequency_and_proportion_of_words_with_letter(letters_and_number: dict, word_list: list):
    """Frequency of use and proportion of words with letter

    :param letters_and_number: letter: number of letters in text { str: int }
    :type word_list: dict
    :param word_list: list of all words from the text
    :type word_list: list[str]

    :rtype: dict
    :return: The key : letter of the alphabet; value :tuple (frequency_of_use_of_letter, fraction_of_words_with_letter)
    """
    # Всего букв
    number_total_letters = sum(letters_and_number.values())

    # Букв нет, возвращаем пустой словарь
    if number_total_letters == 0:
        return {
            letter: (0, 0)
            for letter in letters_and_number.keys()
        }

    return {
        letter:  # Ключ - буква
            (letters_and_number[letter] / number_total_letters,  # tuple[0] - частота использования буквы
             number_words_with_letter(word_list, letter))  # tuple[1] - доля слов с буквой
        for letter in letters_and_number.keys()  # Перебираем буквы
    }


def number_of_paragraphs(text: str):
    """Number of paragraphs in the text

    :param text: text
    :type text: str

    :rtype: int
    :return: Number of paragraphs in the text
    """
    # . — любому символу, кроме новой строки; \S - описывает любой не пробельный символ.
    return len(re.findall(r'.\S.+', text))


def bilingual_word(text: str):
    """Number of words with Russian and English letters

    :param text: text
    :type text: str

    :rtype: int
    :return: count bilingual word
    """
    return len(re.findall(r'[a-z]+\w+[а-я]+|[а-я]+\w+[a-z]+', text))


def text_stat(filename: str):
    """Path, name and extension of the file to be read and statistics calculated

    :param filename: Path, name and extension
    :type filename: str

    :rtype: dict
    :return: statistics
    Contents of the dictionary:

    * letter: (frequency_of_use_of_letter, proportion_of_words_with_letter),
    * word_amount: number of words in the text,
    * paragraph_amount: number of paragraphs in the text,
    * bilingual_word_amount: number of words using letters from both alphabets

    Errors:
    * FileNotFoundError -> return {'error': 'Файл не найден'}
    * Exception -> return {'error': str(e)}
    """
    # Чтение всего файла
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            text = file.read()
    except FileNotFoundError:
        return {'error': 'Файл не найден'}
    except Exception as e:
        return {'error': str(e)}

    # Приводим к нижнему регистру
    text = text.lower()

    # Результирующий словарь
    dictionary_of_text_statistics = {}

    # Получаем list слов
    word_list = word_list_from_text(text)
    # (I) Количество слов
    dictionary_of_text_statistics["word_amount"] = len(word_list)

    # Словарь: буквы и их количество
    letters_and_number = count_of_letter_uses(text)

    # (II) Ключ - буква алфавита, значение – tuple (частота_использования_буквы, доля_слов_с_буквой)
    dictionary_of_text_statistics.update(
        frequency_and_proportion_of_words_with_letter(letters_and_number, word_list)
    )

    # (III) Количество абзацев
    dictionary_of_text_statistics["paragraph_amount"] = number_of_paragraphs(text)

    # (IV)Количество слов с английскими и русскими буквами
    dictionary_of_text_statistics["bilingual_word_amount"] = bilingual_word(text)

    return dictionary_of_text_statistics
