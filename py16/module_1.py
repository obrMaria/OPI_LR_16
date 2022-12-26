#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def dell(a):
    def del_with_tye(type='even'):
        b = []
        if type == "even":
            b = [i for i in a if i % 2 != 0]
            return b
        else:
            b = [i for i in a if i % 2 == 0]
            return b

    return del_with_tye
