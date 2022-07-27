INPUT_FILE = 'Text1.txt'
OUTPUT_FILE = 'words_and_its_frequency.txt'


def main():
    words_list = create_words_list(INPUT_FILE)
    list_without_punctuation = create_words_list_without_punctuation(words_list)
    dic_with_results = dic_with_words_and_its_frequency(list_without_punctuation)
    create_file_with_results(OUTPUT_FILE, dic_with_results)


def create_words_list(name_file):
    with open(name_file) as file:
        text_from_file = file.read()
    words_list = text_from_file.lower().split()

    return words_list


def create_words_list_without_punctuation(words_list):
    words_list_without_punctuation = []
    for word in words_list:
        if word[len(word) - 1] in ',.!?':
            word = word.replace(word[len(word) - 1], '')
        words_list_without_punctuation.append(word)

    return words_list_without_punctuation


def dic_with_words_and_its_frequency(list_of_words):
    dic_words_and_frequency = {}
    value = 0

    for word in list_of_words:
        dic_words_and_frequency[word] = dic_words_and_frequency.setdefault(word, value) + 1
    return dic_words_and_frequency


def create_file_with_results(file_name, dic):
    with open(file_name, 'a') as file:
        for key, value in dic.items():
            file.write(f'Слово "{key}" зустрічається {value} раз(а)\n\n')


main()
