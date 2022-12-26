#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from packet.get_student import get_student
from packet.display_student import display_student
from packet.find_students import find_students

import sys

def main():
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            get_student(students)

        elif command == 'list':
            display_student(students)

        elif command == 'find':
            found = find_students(students)
            display_student(found)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("find - вывод на фамилий и номеров групп студента с оценками 4 и 5 ;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
