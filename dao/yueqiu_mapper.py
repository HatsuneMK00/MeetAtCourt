# -*- coding: utf-8 -*-
# created by makise, 2021/3/17
from dao.utils import need_db

# 参数说明：
# offset 表示数据库中索引的偏移值
from model.YueQiu import YueQiu


@need_db
def select_ten_item_from_offset(cursor, **kwargs):
    query = """select * from yueqiu limit {}, 10""".format(kwargs['offset'])
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    yueqius = []
    for line in result:
        yueqiu = YueQiu(line[0], line[1], line[2], line[3], line[4], line[5])
        yueqius.append(yueqiu)
    return yueqius

if __name__ == '__main__':
    print(select_ten_item_from_offset(offset=0))
