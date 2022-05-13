import sys


name = input('Enter your name: ')
file_name = name + '.txt'
print('Describe yourself: ', end='')
description = sys.stdin.readlines()

cover_file = open('HTML_cover.txt', 'r')
new_file = open(file_name, 'w')
for s in cover_file:
    if 'name' in s:
        s = s.replace('name', name)
    if 'description' in s:
        s = s.replace('description', description[0].rstrip('\n'))
        for i in description[1:]:
            s += '    ' + i
    new_file.write(s)
new_file.close()
cover_file.close()
