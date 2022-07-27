from collections import defaultdict

INPUT_FILE = 'Text1.txt'
OUTPUT_FILE = 'words_and_its_frequency.txt'
ALPHABET_UKR = 'абвгґдеєжзиійїклмнопрстуфхцчщьюя'


def main():
    words_list = create_words_list(INPUT_FILE)
    dic_with_results = dic_with_words_and_its_frequency(words_list)
    create_file_with_results(OUTPUT_FILE, dic_with_results)


def create_words_list(name_file):
    with open(name_file) as file:
        text_from_file = file.read()
        words_list = []
        word = ''

        for letter in text_from_file.lower():
            if letter in ALPHABET_UKR:
                word += letter
            else:
                if word != '':
                    words_list.append(word)
                    word = ''

    return words_list


def dic_with_words_and_its_frequency(list_of_words):
    dic_words_and_frequency = defaultdict(int)

    for word in list_of_words:
        dic_words_and_frequency[word] += 1
    return dic_words_and_frequency


def create_file_with_results(file_name, dic):
    with open(file_name, 'a') as file:
        for key, value in dic.items():
            file.write(f'Слово "{key}" зустрічається {value} раз(а)\n\n')


main()
