def to_weird_case(string):
    massive_of_words = string.split()
    changed_words = []
    for each_word in massive_of_words:
        weird_case_word = ''
        for i in range(len(each_word)):
            if i % 2 == 0:
                weird_case_word += each_word[i].upper()
            else:
                weird_case_word += each_word[i].lower()
        changed_words.append(weird_case_word)
    return ' '.join(changed_words)


print(to_weird_case('This is a test'))