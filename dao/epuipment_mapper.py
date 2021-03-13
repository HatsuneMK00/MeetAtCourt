# -*- coding: utf-8 -*-
# created by makise, 2021/3/12

from dao.utils import need_db


@need_db
def test_connection(cursor, **kwargs):
    query = """select * from test"""
    cursor.execute(query)
    result = cursor.fetchall()
    print(len(result))
    print(len(result[0]))
    print(result[0])
    print(result[0][1])
    print(result)


if __name__ == '__main__':
    test_connection()
