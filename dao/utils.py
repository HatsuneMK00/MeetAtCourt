# -*- coding: utf-8 -*-
# created by makise, 2021/3/12
# todo 添加连接池
import pymysql

from dao.settings import DB_DATABASE_URL, DB_DEFAULT_DATABASE, DB_PASSWORD, DB_USERNAME


def db_connect():
    connection = pymysql.connect(
        DB_DATABASE_URL,
        DB_USERNAME,
        DB_PASSWORD,
        DB_DEFAULT_DATABASE)
    return connection


def db_disconnect(connection):
    connection.close()


# select_query是sql语句
# 返回的result是个二维数组
# 包装了数据库连接断开的操作，调用时只考虑sql语句即可
# result的第一维对应数据库中每一行 第二维对应每一列
# 例如，搜索到的结果有30个数据，那么len(result)=30
# 每个数据（每一行）有5个字段，那么len(result[0])=5
def select_query_better(select_query):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute(select_query)
    result = cursor.fetchall()
    cursor.close()
    db_disconnect(connection)
    return result
