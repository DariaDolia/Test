import sys


name = input('Enter your name: ')
file_name = name + '.txt'
string = input(f'Describe yourself: \n')
description = []
while string != '':                 # decide to use your methods
    description.append(string)      # for multiply entry
    string = input()
print(description)

cover_file = open('HTML_cover.txt', 'r')
new_file = open(file_name, 'w')
for s in cover_file:
    if 'name' in s:
        s = s.replace('name', name)
    if 'description' in s:
        s = s.replace('description', description[0].rstrip('\n'))
        s += ''.join([f'    {i}\n' for i in description[1:]])
    new_file.write(s)
new_file.close()
cover_file.close()
