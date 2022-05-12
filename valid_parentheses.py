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


def valid_parentheses_2(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    return False


print(valid_parentheses_2("()"))


def valid_parentheses_3(string):
    braces_string = ''.join([s for s in string if s in '()'])
    while '()' in braces_string:
        braces_string = braces_string.replace('()', '', 1)
    return not braces_string


print(valid_parentheses_3("()"))


assert valid_parentheses_3(")(()))") is False
assert valid_parentheses_3("(())((()())())") is True
assert valid_parentheses_3("(") is False
assert valid_parentheses_3(")test") is False
assert valid_parentheses_3('') is True
assert valid_parentheses_3("hi())(") is False
assert valid_parentheses_3("hi(hi)()") is True


