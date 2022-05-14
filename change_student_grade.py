import os


def check_student_name():
    origin_file = open('student_list.txt', 'r')
    while True:
        student_name = input('Enter a student name to change grade: ')
        line = origin_file.readline()
        has_name = False
        while line != '':
            if line.startswith(student_name):
                print(f'Сейчас {line}')
                has_name = True
                break
            line = origin_file.readline()
        if not has_name:
            print('Not find this name in the list. Try again\n')
            origin_file.seek(0)
        else:
            origin_file.close()
            return student_name


def check_new_grade(student_name):
    while True:
        try:
            new_grade = int(input(f'Enter a new grande for {student_name}: '))
        except ValueError:
            print('Please, enter only numbers\n')
            continue
        if new_grade not in range(0, 101):
            print('Grade should be in range from 0 to 100\n')
        else:
            return new_grade


def change_grade(student_name, new_grade):
    origin_file = open('student_list.txt', 'r')
    temp_file = open('temp.txt', 'w')
    for line in origin_file:
        if line.startswith(student_name):
            if ' ' in line:
                name_grade_mas = line.split()
            else:
                name_grade_mas = line.split('\n')
            line = f'{name_grade_mas[0]} {new_grade}\n'
        temp_file.write(line)
    origin_file.close()
    temp_file.close()

    os.remove('student_list.txt')
    os.rename('temp.txt', 'student_list.txt')


def main():
    student_name = check_student_name()
    new_grade = check_new_grade(student_name)
    change_grade(student_name, new_grade)


main()
