#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def range_calculator(data: list) -> int:
    result = (data[0] * 100)/(data[0] + data[1])

    if 0 <= result <= 20:
        result = 1

    elif 20 < result <= 40:
        result = 2

    elif 40 < result <= 60:
        result = 3

    elif 60 < result <= 80:
        result = 4

    elif 80 < result <= 100:
        result = 5

    return result
