#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def get_student(staff):
    # Запросить данные о студенте.
    name = input("Фамилия и инициалы? ")
    group = input("Номер группы? ")
    grade = list(map(int, input("введите свои оценки: ").split()))

    # Создать словарь.
    student = {
        'name': name,
        'group': group,
        'grade': grade,
    }
    # Добавить словарь в список.
    staff.append(student)

    # Отсортировать список в случае необходимости.
    if len(staff) > 1:
        staff.sort(key=lambda item: item.get('group')[::-1])
