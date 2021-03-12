# -*- coding: utf-8 -*-
# created by makise, 2021/3/12

from dao.utils import select_query_better


def test_connection():
    query = """select * from test"""
    result = select_query_better(query)
    print(len(result))
    print(len(result[0]))
    print(result[0])
    print(result[0][1])

    print(result)
