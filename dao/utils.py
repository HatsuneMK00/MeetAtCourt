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


# 该装饰器向被装饰的函数提供一个参数cursor，被装饰参数需要声明该参数并可以直接使用
def need_db(func):
    def wrapper(**kwargs):
        connection = db_connect()
        cursor = connection.cursor()
        func(cursor, **kwargs)
        cursor.close()
        connection.close()
    return wrapper
