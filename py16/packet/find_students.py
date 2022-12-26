#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def find_students(staff):
    result = []
    count = 0
    for student in staff:
        grade = student.get('grade', '')
        if sum(grade) / (len(grade)) >= 4.0:
            result.append(student)
            count += 1

    return result
