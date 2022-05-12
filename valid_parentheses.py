
def valid_parentheses(string):
    left_braces = string.count('(')
    right_braces = string.count(')')
    count = 0
    braces_string = ''.join([s for s in string if s in '()'])
    lenght = len(braces_string)
    if left_braces == right_braces:
        for i in range(lenght):
            if braces_string.find('(') < braces_string.find(')'):
                count += 1
            braces_string = braces_string.replace('(', '', 1)
            braces_string = braces_string.replace(')', '', 1)
        if count == lenght/2:
            return True
    return False


print(valid_parentheses('(())((())'))
